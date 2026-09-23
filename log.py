#Abstração
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError('Implemente o método Log')

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_succes(self, msg):
        return self._log(f'Succes: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_formatada= f'{msg}({self.__class__.__name__})'
        print('Salvando no log:', msg)
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg}({self.__class__.__name__})')

if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Oooooooooooola')
    lp.log_succes('aaaaaaaaaaaaaaa')
    lf = LogFileMixin()
    lf.log_error('Oooooooooooola')
    lf.log_succes('aaaaaaaaaaaaaaa')
