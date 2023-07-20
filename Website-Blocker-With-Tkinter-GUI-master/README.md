# Website-Blocker-With-Tkinter-GUI
Website Blocker is a tool that denies access to websites permanently or by schedule. To use the internet safely we can block all websites from unwanted categories.
Website Blocker Python Project

The objective of Website Blocker python project is to block the given websites from any device. This project will help the user to stay away from their distraction by blocking websites from their device so that they can not open them.

In this Python Website Blocker Project, the user can enter multiple websites to block, and then clicking on the block button will check the condition that if the website already blocked then print ‘already blocked’ else blocked all that websites and print ‘blocked’.

Project Prerequisites

To implement website blocker project, we will use the basic concepts of Python and Tkinter library.

Tkinter is a standard GUI Python library. It is one of the fastest and easiest ways to build GUI applications using Tkinter.

Steps to build Website blocker Python Project:

    1:Importing the module
    2:Create the display window
    3:Create an entry widget
    4:Define function
    5:Create a block button

1:

     We import modules from tkinter library.

2:

     We use tkinter library to create a window where we’ll enter our text.

3:

     Create an entry widget.
     
          host_path stores the path of our host file.
          ip_address stores the IP address used by localhost.
          Text() widget is used for multi-line text areas.
          wrap = WORD will break the line after the last word.
          padx puts an extra bit space on left and right side of the widget
          pady puts extra space on top and bottom side of the widget.

4:

     Define function.
     
          website_lists get all the Websites to enter by the users.
          website_list(lists.split(“,”)) split the content of the lists by comma and then convert it into list ad store it into Website.
          with open – The with open statement open the file and it will automatically close the file handler when we are done with it.
          r+ will use to open a file for reading and writing.
          If the website is already in file_content then print a label with text already blocked.
          Else it will block all the given website and print label of text ‘Blocked’.

5:

     When we click on the Block button it will call the Blocker function.
     
          Button() – used to display button on our window.
          command – called when we click the button.
          activebackground – sets the background color to use when the button is click.
