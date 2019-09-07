// stdafx.h : include file for standard system include files,
// or project specific include files that are used frequently,
// but are changed infrequently

#pragma once

#ifndef STRICT
#define STRICT
#endif

#include "targetver.h"

#define _ATL_APARTMENT_THREADED
#define _ATL_NO_AUTOMATIC_NAMESPACE

#define _ATL_CSTRING_EXPLICIT_CONSTRUCTORS	// some CString constructors will be explicit

#include "resource.h"
#include <atlbase.h>
#include <atlcom.h>
#include <atlctl.h>

using namespace ATL;
//#import "C:\Program Files\Common Files\DESIGNER\MSADDNDR.DLL" raw_interfaces_only, raw_native_types, no_namespace, named_guids, auto_search
#import "libid:AC0714F2-3D04-11D1-AE7D-00A0C90F26F4" raw_interfaces_only, raw_native_types, no_namespace, named_guids, auto_search
