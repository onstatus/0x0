

 ################################################################################
 # This is a configuration file for 0x0 / The Null Pointer                      #
 #                                                                              #
 # The default values here are set to generally reasonable defaults, but a      #
 # couple of things need your attention.  Specifically, make sure you set       #
 # SQLALCHEMY_DATABASE_URI.  You'll also probably want to configure             #
 # FHOST_USE_X_SENDFILE and FHOST_USE_X_ACCEL_REDIRECT to match your webserver. #
 #                                                                              #
 # Need help, or find anything confusing?  Try opening up an issue!             #
 # https://git.0x0.st/mia/0x0/issues/new                                        #
 ################################################################################



# The database URL for the database 0x0 should use
#
# See https://docs.sqlalchemy.org/en/20/core/engines.html#backend-specific-urls
# for help configuring these for your database.
#
# For small and medium servers, it's plenty sufficient to just use an sqlite
# database.  In this case, the database URI you want to use is just
#
# sqlite:/// + /path/to/your/database.db
#
# Until https://git.0x0.st/mia/0x0/issues/70 is resolved, it's recommended that
# any sqlite databases use an absolute path, as relative paths aren't consistently
# resolved.
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + '/path/to/database.sqlite'


# The maximum allowable upload size, in bytes
#
# Keep in mind that this affects the expiration of files as well!  The closer a
# file is to the max content length, the less time it will last before being
# deleted.
MAX_CONTENT_LENGTH = 256 * 1024 * 1024 # Default: 256MiB


# The maximum length of URLs we'll shorten, in characters
#
# If a user tries to submit a URL longer than this, we'll reject their request
# with a 414 REQUEST URI TOO LONG.
MAX_URL_LENGTH = 4096


# The minimum and maximum amount of time we'll retain a file for
#
# Small files (nearing zero bytes) are stored for the longest possible expiration date,
# while larger files (nearing MAX_CONTENT_LENGTH bytes) are stored for the shortest amount
# of time.  Values between these two extremes are interpolated with an exponential curve,
# like the one shown on the index page.
#
# All times are in milliseconds.  If you want all files to be stored for the same amount
# of time, set these to the same value.
FHOST_MIN_EXPIRATION = 30  * 24 * 60 * 60 * 1000
FHOST_MAX_EXPIRATION = 365 * 24 * 60 * 60 * 1000


# This should be detected automatically when running behind a reverse proxy, but needs
# to be set for URL resolution to work in e.g. the moderation UI.
# SERVER_NAME = "example.com"


# Specifies which graphics protocol to use for the media previews in the moderation UI.
# Requires pympv with libmpv >= 0.36.0 and terminal support.
# Available choices are "sixel" and "kitty".
# MOD_PREVIEW_PROTO = "sixel"


# Use the X-SENDFILE header to speed up serving files w/ compatible webservers
#
# Some webservers can be configured use the X-Sendfile header to handle sending
# large files on behalf of the application.  If your server is setup to do
# this, set this variable to True
USE_X_SENDFILE = False


# Use X-Accel-Redirect to speed up serving files w/ compatible webservers
#
# Other webservers, like nginx and Caddy, use the X-Accel-Redirect header to
# accomplish a very similar thing to X-Sendfile (above).  If your webserver is
# configured to do this, set this variable to True
#
# Note:  It's recommended that you use either X-Sendfile or X-Accel-Redirect
# when you deploy in production.
FHOST_USE_X_ACCEL_REDIRECT = True # expect nginx by default


# The directory that 0x0 should store uploaded files in
#
# Whenever a file is uploaded to 0x0, we store it here!  Relative paths are
# resolved relative to the working directory that 0x0 is being run from.
FHOST_STORAGE_PATH = "up"


# The maximum acceptable user-specified file extension
#
# When a user uploads a file, in most cases, we keep the file extension they
# provide.  But!  If the specified file extension is longer than
# FHOST_MAX_EXT_LENGTH, we truncate it.  So if a user tries to upload the file
# "myfile.withareallongext", but FHOST_MAX_EXT_LENGTH is set to 9, then the
# extension that we keep is ".withareal"
FHOST_MAX_EXT_LENGTH = 9


# The number of bytes used for "secret" URLs
#
# When a user uploads a file with the "secret" option, 0x0 generates a string
# from this many bytes of random data. It is base64-encoded, so on average
# each byte results in approximately 1.3 characters.
FHOST_SECRET_BYTES = 16

# A list of filetypes to use when the uploader doesn't specify one
#
# When a user uploads a file with no file extension, we try to find an extension that
# works for that file.  This configuration option is the first thing that we check.  If
# the type of a file without an extension is in this dict, then it'll be used as the file
# extension for that file. Otherwise, we try to pick something sensible from libmagic's
# database.
#
# For example, if the user uploads "myfile" with no extension, and the file is a jpeg
# image, the file will get a URL like "eAa.jpg"
#
# For a list of MIME types you can use in this list, check
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
FHOST_EXT_OVERRIDE = {
    "audio/flac" : ".flac",
    "image/gif" : ".gif",
    "image/jpeg" : ".jpg",
    "image/png" : ".png",
    "image/svg+xml" : ".svg",
    "video/webm" : ".webm",
    "video/x-matroska" : ".mkv",
    "application/octet-stream" : ".bin",
    "text/plain" : ".log",
    "text/plain" : ".txt",
    "text/x-diff" : ".diff",
}


# Control which files aren't allowed to be uploaded
#
# Certain kinds of files are never accepted.  If the file claims to be one of
# these types of files, or if we look at the contents of the file and it looks
# like one of these filetypes, then we reject the file outright with a 415
# UNSUPPORTED MEDIA EXCEPTION
FHOST_MIME_BLACKLIST = [
    "application/x-dosexec",
    "application/java-archive",
    "application/java-vm"
]


# A list of IP addresses which are blacklisted from uploading files
#
# Can be set to the path of a file with an IP address on each line.  The file
# can also include comment lines using a pound sign (#).  Paths are resolved
# relative to the instance/ directory.
#
# If this is set to None, then no IP blacklist will be consulted.
FHOST_UPLOAD_BLACKLIST = None


# Enables support for detecting NSFW images
#
# Consult README.md for additional dependencies before setting to True
NSFW_DETECT = False


# The cutoff for when an image is considered NFSW
#
# When the NSFW detection algorithm generates an output higher than this
# number, an image is considered to be NSFW.  NSFW images aren't declined, but
# are marked as NSFW.
#
# If NSFW_DETECT is set to False, then this has no effect.
NSFW_THRESHOLD = 0.608


# If you want to scan files for viruses using ClamAV, specify the socket used
# for connections here. You will need the clamd module.
# Since this can take a very long time on larger files, it is not done
# immediately but every time you run the vscan command. It is recommended to
# configure a systemd timer or cronjob to do this periodically.
# Remember to adjust your size limits in clamd.conf, including StreamMaxLength!
#
# Example:
# from clamd import ClamdUnixSocket
# VSCAN_SOCKET = ClamdUnixSocket("/run/clamav/clamd-socket")

# This is the directory that files flagged as malicious are moved to.
# Relative paths are resolved relative to the working directory
# of the 0x0 process.
VSCAN_QUARANTINE_PATH = "quarantine"

# Since updated virus definitions might catch some files that were previously
# reported as clean, you may want to rescan old files periodically.
# Set this to a datetime.timedelta to specify the frequency, or None to
# disable rescanning.
from datetime import timedelta
VSCAN_INTERVAL = timedelta(days=7)

# Some files flagged by ClamAV are usually not malicious, especially if the
# DetectPUA option is enabled in clamd.conf. This is a list of signatures
# that will be ignored.
VSCAN_IGNORE = [
    "Eicar-Test-Signature",
    "PUA.Win.Packer.XmMusicFile",
]

# A list of all characters which can appear in a URL
#
# If this list is too short, then URLs can very quickly become long.
# Generally, the default value for this should work for basically all usecases.
URL_ALPHABET = "DEQhd2uFteibPwq0SWBInTpA_jcZL5GKz3YCR14Ulk87Jors9vNHgfaOmMXy6Vx-"


 #################################################################################
 # CONGRATULATIONS!  You made it all the way through!                            #
 # If you want to go even further to customize your instance, try checking out   #
 # the templates in the templates/ directory to customize your landing page, 404 #
 # page, and other error pages.                                                  #
 #################################################################################

