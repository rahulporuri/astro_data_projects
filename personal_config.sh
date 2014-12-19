#! /bin/bash

echo "the numpy, matplotlib, astropy libraries used in python, gnuplot, vim and git will be installed"
read -n1 -r -p "press enter to continue or q to quit" key
echo ""
if [ "$key" = "q" ]; then
	echo "you have quit the installation"
elif [ "$key" = "" ]; then
	echo ""
	echo "installing python-numpy package"
	echo ""
	sudo apt-get install python-numpy
	echo ""
	echo "installing python-matplotlib package"
	echo ""
	sudo apt-get install python-matplotlib
	echo ""
	echo "installing python-astropy"
	echo ""
	sudo apt-get install python-astropy
	echo ""
	echo "installing gnuplot"
	echo ""
	sudo apt-get install gnuplot
	echo ""
	echo "installing git"
	echo ""
	sudo apt-get install git
	echo "having installed git, we strongly suggest you create an account on github here - https://github.com/"
	echo "and follow the instructions provided here - https://help.github.com/articles/generating-ssh-keys/  to link your system to your github account."
	echo "for now, the repository for the workshop is available at - https://github.com/rahulporuri/astro_data_projects"
	echo ""
	echo "installing vim"
	echo ""
	sudo apt-get install vim
	echo "just a reminder, $ vim foo.bar will open the file, i to insert changes in the file, esc to escape the editing mode,"
	echo ":w can be used to save the file, :q to exit. Take note that :q! can be used to quit without saving"
	echo "mail us if any problems arise during this installation"
	echo ""
fi
