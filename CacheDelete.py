import WriteFile as wf
import GetInformation as g
import Main as m

class CacheDelete:

    def deleteCache(self, student_id):
        after_cache = []
        cache = g.GetInformation().getInfo('input/cache_file.tsv')
        [after_cache.append(value) for value in cache if student_id[0] != value[0]]
        wf.WriteFile('input/cache_file.tsv').writeInFile(after_cache, m.Main().headers)
        if len(cache) == len(after_cache):
            return m.Main().warning + str(student_id[0]) + " student record does not exist to delete" + m.Main().end
        return m.Main().update + str(student_id[0]) + " student record deleted" + m.Main().end
