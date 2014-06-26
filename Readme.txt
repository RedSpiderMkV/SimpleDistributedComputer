Simple distributed computer.

Currently in development, work in progress.

Intended to simply send task to another (powerful) machine to perform calculation and then return the result
to the sender.

Much work remains to be done and bugs to be fixed.

Most obvious bug at present, spawning a new thread and then terminating listener leaves an orphaned thread hanging
around, preventing the application from launching again without ending orphaned process.