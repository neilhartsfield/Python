import sys
from evtx import EvtxParser


def convert_evtx_to_txt(evtx_file, txt_file):
    # Open the EVTX file and create a new TXT file
    with open(evtx_file, "rb") as in_file, open(txt_file, "w") as out_file:
        # Parse the EVTX file
        for record in EvtxParser(in_file):
            # Extract the XML data from the record
            xml_string = record.xml()
            # Write the XML data to the TXT file
            out_file.write(xml_string)
            out_file.write("\n")


if __name__ == "__main__":
    # Get the input and output filenames from the command line arguments
    evtx_file = sys.argv[1]
    txt_file = sys.argv[2]
    # Convert the EVTX file to a TXT file
    convert_evtx_to_txt(evtx_file, txt_file)
