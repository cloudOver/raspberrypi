window.coreUrl = "http://192.168.27.254:8000/";
window.vncHost = "192.168.27.254";
window.vncPort = 8000;
window.vncPrefix = "/webvnc/";

window.debug = false;

// Installed applications. Put 'home' controller at end of this list. Otherwise, it will catch all urls
window.modules = ['home', 'vm', 'image', 'network', 'coretalk', 'account', 'coredhcp', 'corevpn', 'thunderscript'];
