ifeq ($(OS),Windows_NT)
	BUILD=MSBuild.exe
	EXEC=
	RM=del /Q /F
	SLASH=\\
	NUNIT="C:\Program Files (x86)\NUnit.org\nunit-console\nunit3-console.exe"
else
	BUILD=xbuild
	RM=rm -rf
	SLASH=/
	EXEC=mono
	NUGET=/usr/local/bin/nuget.exe
	NUNIT=/opt/nunit-3.0.1/bin/nunit3-console.exe
endif

SOLUTION:=$(wildcard *.sln)
TESTPROJ:=$(wildcard *Tests/*.csproj)

build: nuget
	@$(BUILD) /p:WarningLevel=0 /p:TargetFrameworkVersion=v4.5.1 /verbosity:quiet $(SOLUTION)

nuget:
	@$(EXEC) $(NUGET) restore $(SOLUTION)

test: build $(TESTPROJ)
ifeq ("$(wildcard $(TESTPROJ))","")
	@echo WARN: no test project found
else
	@$(EXEC) $(NUNIT) $(TESTPROJ)
endif

clean:
	$(RM) $(wildcard */bin/*)
	$(RM) $(wildcard */obj/*)

