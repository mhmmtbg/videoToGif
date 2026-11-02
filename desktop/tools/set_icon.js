const fs=require('fs'),R=require('resedit');
const [exePath,icoPath]=process.argv.slice(2);
const exe=R.NtExecutable.from(fs.readFileSync(exePath));const res=R.NtExecutableResource.from(exe);
const ico=R.Data.IconFile.from(fs.readFileSync(icoPath));
const groups=R.Resource.IconGroupEntry.fromEntries(res.entries);
console.log('groups',groups.map(g=>g.id+'/'+g.lang));
const targets=groups.length?groups.map(g=>[g.id,g.lang]):[[1,1033]];
for(const [id,lang] of targets) R.Resource.IconGroupEntry.replaceIconsForResource(res.entries,id,lang,ico.icons.map(i=>i.data));
const vis=R.Resource.VersionInfo.fromEntries(res.entries);
if(vis.length){const v=vis[0];for(const l of v.getAllLanguagesForStringValues()){v.setStringValues(l,{ProductName:'GIF Atölyesi',FileDescription:'GIF Atölyesi',InternalName:'GifAtolyesi',OriginalFilename:'GifAtolyesi.exe',CompanyName:'',LegalCopyright:''});}v.outputToResourceEntries(res.entries);}
res.outputResource(exe);fs.writeFileSync(exePath,Buffer.from(exe.generate()));console.log('ok');
