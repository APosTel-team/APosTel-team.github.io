# Full path to vdat.exe
vdat_exe <- "C:/Program Files/Vemco/Fathom/vdat.exe"
 
# List of VRL files to convert
vrl_files <- list.files(path="C:/Users/Documents/path_to_vrl_files/", pattern = "*.vrl", full.names = TRUE)
 
# Do conversion
system2(
  vdat_exe,
  c(
    "convert",
    "--timec=default",        # - Use default linear time correction
    "--format=csv.fathom",    # - Convert to Fathom CSV
    "--output=.",             # - Place output CSV files in current working directory
    vrl_files
    )
)