# If you have problems with the gkt+-3.0 installation (that is needed
# for running the non trojan code horse of trj) you can try running this script
# with administration rights. This script will try to install all the dependencies
# that are needed for setting up gtk3.0
#
# Use at your own risk
#
#   Usage:
#       sudo su
#       sh gtk.sh
#       exit
#
#   Or in the same line 
#       sudo su && sh gtk.sh && exit
#
# For more information check: github.com/pblcc/trj
ROUTE="/usr/lib/x86_64-linux-gnu/pkgconfig/gtk+-3.0.pc"
# - - - - - DON'T TOUCH ANYTHING FROM HERE TO THE END OF THE FILE
if ! [ -x "$(command -v pkg-config) "]; then
  echo "Pkg config is not installed in this system"
  exit 1
fi
# Check if the route of the gtk.pc file exists and do a thing or anoter if it does.
if [ -f "$ROUTE" ]; then
  pkg-config --debug --modversion gtk+-3.0
fi
export PKG_CONFIG_PATH="$(ROUTE)"
pkg-config --modversion gtk+-3.0


