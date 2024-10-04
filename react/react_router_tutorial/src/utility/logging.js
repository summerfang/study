const LogLevel = {
    DEBUG: 'debug',
    INFO: 'info',
    WARN: 'warn',
    ERROR: 'error'
  };
  
  class Logger {
    constructor(level = LogLevel.DEBUG) {
      this.logLevel = level;
    }
  
    log(message, level = LogLevel.DEBUG) {
      if (this.shouldLog(level)) {
        console.log(`[${__filename} {} ${new Date().toISOString()}] [${level.toUpperCase()}] - ${message}`);
      }
    }
  
    info(message) {
      this.log(message, LogLevel.INFO);
    }
  
    warn(message) {
      this.log(message, LogLevel.WARN);
    }
  
    error(message) {
      this.log(message, LogLevel.ERROR);
    }
  
    debug(message) {
      this.log(message, LogLevel.DEBUG);
    }
  
    shouldLog(level) {
      const levels = [LogLevel.DEBUG, LogLevel.INFO, LogLevel.WARN, LogLevel.ERROR];
      return levels.indexOf(level) >= levels.indexOf(this.logLevel);
    }
  }
  
  // Usage:
  const logger = new Logger(LogLevel.INFO);
  logger.debug('This is a debug message'); // Won't be logged due to log level
  logger.info('This is an info message');
  logger.warn('This is a warning');
  logger.error('This is an error message');
  