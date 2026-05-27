---
aliases:
  - obsidian/tweaks/dvjs-find-bad-yaml
author:
  - Sascha D. Kasper
source: https://blog.sascha-kasper.com/DVJS---Find-bad-YAML
description: Find notes with broken or corrupt YAML frontmatter in your Obsidian vault using this DataviewJS query.
cover:
date: 2024-04-12
draft: false
categories:
  - obsidian
  - dataview
cssclasses:
tags:
  - obsidian
  - dataview
created: 2024-04-12T09:58
updated: 2026-01-09T11:58
---

# Setup
This is a DataviewJS query to find files that have "bad" - i.e. corrupt - frontmatter.
# Code
Don't forget to start and end the code block with three backticks.

```text
dataviewjs

const result = []

for (let [fname, fcache] of Object.entries(dv.app.metadataCache.fileCache)) {
  // fname is the filename
  // fcache is the entry from metadataCache.fileCache
  // mcache is the actual metadataCache.metadataCache entry
  const mcache = dv.app.metadataCache.metadataCache[fcache.hash]
  
  if ( (mcache && !mcache.frontmatter &&
        mcache.hasOwnProperty("sections") &&
        mcache["sections"].some(s => s.type == "yaml"))
     || ( mcache && mcache.frontmatter && mcache.frontmatter.notvalid ) 
     ) {
    const yamlIndex = mcache["sections"].findIndex(s => s.type == "yaml")
    let yamlStart, yamlEnd
  
    // Pull out start and end, if section is found
    if ( yamlIndex !== -1 ) {
      yamlStart = mcache["sections"][yamlIndex]?.position.start.line
      yamlEnd = mcache["sections"][yamlIndex]?.position.end.line
    }
    
    // Determine the cause of the faulty frontmatter
    let cause
    
    if ( mcache.frontmatter?.notvalid )        cause = "Not valid"
    else if ( yamlIndex == -1 )                cause = "NO yaml"
    else if ( yamlStart == 0 && yamlEnd == 1 ) cause = "Empty"
    else cause = "Bad"
    
    result.push([dv.fileLink(fname), cause, yamlStart ?? "", yamlEnd ?? ""])
    // console.log(fname, " » ", mcache) 
  }   
  //console.log(fname, " » ", fcache, "\n  »» ", mcache)
}

dv.table(["File", "Yaml status", "Start", "End"], result)
```
# Result

![[DVJS - Find bad YAML.webp|Dataview table flagging one file with bad YAML status and line numbers]]

# Source
[Is it possible to find all files in vault with bad YAML? - Help - Obsidian Forum](https://forum.obsidian.md/t/is-it-possible-to-find-all-files-in-vault-with-bad-yaml/77698/3)
Author: https://forum.obsidian.md/u/holroy
