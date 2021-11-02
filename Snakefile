# User config
configfile: "build_comp_obj_mass_from_top.yml"


# Import the showyourwork module
module showyourwork:
    snakefile:
        "showyourwork/workflow/Snakefile"
    config:
        config

# Use all default rules
use rule * from showyourwork
