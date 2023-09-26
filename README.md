# Automated HandBrake Batch Ripping

This program grabs information from various YAML files and one CSV file and sends a command to HandBrakeCLI based on that information to rip specified titles off of disk images. It is designed specifically to speed up the ripping of TV show collector's editions on DVDs or Blu-Rays, using the syntax of c#d#t#.iso:
- c# = case number
- d# = disk number
- t# = title number
This is also the syntax used in the CSV file that contains a list of all titles on the disk, regardless if they will be ripped. Selecting of titles to rip is done via the case#/disk#.yml file, where metadata about the title is also stored.

Default rip profiles for audio, video, filters, dimensions, and subtitles *(wip)* are stored in profiles/(profileName).yml. 

Currently, the only releases available are for Windows, because that's what I use for transcoding (go NVENC!), but I will be publishing releases for other platforms once I have more time — and once this is more complete. However, because it's just Python 3 source, it will run on whatever platform can run HandBrakeCLI and Python. I believe I programmed it to look for system-wide installs of HandBrakeCLI in non-Windows OSs *as long as the `Executable Path:` key in ['settings.yml'] is set to `Unix`.* Also, if excecuting from source, `pyyaml` must be installed. It can be easily installed via `pip install pyyaml`.



# Note for Windows users:

The HandBrakeCLI executable should be placed in `/HandBrake/HandBrakeCLI.exe`, where `/` is the root of the release folder. If you would like to use a different location, you must change the `Executable Path:` key in [`settings.yml`].
