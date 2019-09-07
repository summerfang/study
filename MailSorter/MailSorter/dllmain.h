// dllmain.h : Declaration of module class.

class CMailSorterModule : public CAtlDllModuleT< CMailSorterModule >
{
public :
	DECLARE_LIBID(LIBID_MailSorterLib)
	DECLARE_REGISTRY_APPID_RESOURCEID(IDR_MAILSORTER, "{E52545E2-4092-4B3B-A6E4-287FFB1D7A9A}")
};

extern class CMailSorterModule _AtlModule;
