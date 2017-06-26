import GetInformation as g
from datetime import datetime
import WriteFile as wf
import Main as m

class CacheUpdate:

    def updateCache(self, details):
        after_cache = []
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cache = g.GetInformation().getInfo('input/cache_file.tsv')
        details = g.GetInformation().getSpecificInfo('input/student_database.tsv', details[0])
        try:
            [after_cache.append(value) for value in cache if details[0] != value[0]]
            if len(after_cache) == 20:
                after_cache = sorted(after_cache, key=lambda t: t[-1])
                del after_cache[0]
            if isinstance(details, list):
                details.append(time)
                after_cache.append(details)
                after_cache = sorted(after_cache, key=lambda t: t[2])
                wf.WriteFile('input/cache_file.tsv').writeInFile(after_cache, m.Main().headers)
                return m.Main().update + "Data updated" + m.Main().end
            else:
                return m.Main().warning + details + m.Main().end
        except:
            return m.Main().warning + "An Error has occurred" + m.Main().end

