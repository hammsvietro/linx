import DumpManager
import DumpOrganizer

dump = DumpManager.GetDump()

dump = DumpOrganizer.NewDump(dump)

DumpOrganizer.jsonWriter(dump)
