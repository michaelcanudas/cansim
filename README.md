# cansim

cansim is a cli application developed for easy simulation and testing of nodes on a CAN bus network.

## features

- send a frame over the can bus
  - create message in the cli
  - pre-made messages for quick testing
- receive frames on the can bus
  - live feed of all frames
  - breakpoint tools for analyzing specific farames

## requirements

cansim uses gs_usb to translate frames to signals

- [gs_usb](https://pypi.org/project/gs-usb/) - the backend for cansim
- [wsl](https://learn.microsoft.com/en-us/windows/wsl/install) - works best on linux

## use

simply run the program and follow the menu options
```
# can sim #

  (0) receive
  (1) send
  (2) help
  (3) <exit>

response (number): __
```

you can navigate through the menus before selecting a simulation option.

## development

cansim was developed for the [yale bdr](https://bulldogsracing.com) team.

## License

we are using an [mit](https://en.wikipedia.org/wiki/MIT_License) license :)

*boola boola*