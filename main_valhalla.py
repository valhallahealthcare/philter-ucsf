import argparse
import distutils.util
import re 
import pickle
from philter import Philter
import gzip
import json

run_eval = False
verbose = False

# ap.add_argument("-i", "--input", default="./data/i2b2_notes/",
#                 help="Path to the directory or the file that contains the PHI note, the default is ./data/i2b2_notes/",
#                 type=str)
input_dir = None

# ap.add_argument("-o", "--output", default="./data/i2b2_results/",
#                 help="Path to the directory to save the PHI-reduced notes in, the default is ./data/i2b2_results/",
#                 type=str)
output_dir = None

# Define format of annotation, allowed values are \"asterisk\", \"i2b2\". 
# "Valhalla" format
output_format = "Valhalla"#"i2b2"

# Default filters.
filters_format = "./configs/philter_delta.json"

# ap.add_argument("--cachepos", default=None,
#                 help="Path to a directoy to store/load the pos data for all notes. If no path is specified then memory caching will be used.",
#                 type=str)
cache_pos = None

philter_config = {
    "verbose":verbose,
    "run_eval":run_eval,
    "finpath":input_dir,
    "foutpath":output_dir,
    "outformat":output_format,
    "filters":filters_format,
    "cachepos":cachepos,
    "text": text
}

filterer = Philter(philter_config)

def philter_phi_tags(text):

    #map any sets, pos and regex groups we have in our config
    # Newly added method by Valhalla Healthcare.
    filtered_text = filterer.map_coordinates_text(text)
    
    #transform the data 
    #Priority order is maintained in the pattern list
    # Newly added method by Valhalla Healthcare.
    filtered_text = filterer.transform_text(filtered_text)

    return filtered_text



# error analysis
        
# if __name__ == "__main__":
#     main()
