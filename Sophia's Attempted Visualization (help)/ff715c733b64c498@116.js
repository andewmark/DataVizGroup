function _1(md){return(
md`# World Bank Environment Data
`
)}

function _2(md){return(
md` i’m thinking of doing a scatterplot of sanitation rate for the x axis and mortality rate for the y and just each plot representing the value for each country
 `
)}

function _environmentRaw20213(__query,FileAttachment,invalidation){return(
__query(FileAttachment("environment-raw-2021@3.csv"),{from:{table:"environment-raw-2021"},sort:[],slice:{to:null,from:null},filter:[],select:{columns:null}},invalidation)
)}

function _environmentData(FileAttachment){return(
FileAttachment("environment-raw-2021@3.csv").csv({ typed: true })
)}

function _filteredMortality(environmentData){return(
environmentData
  .filter(d => d[""] === "Mortality rate attributed to unsafe water, unsafe sanitation and lack of hygiene (per 100,000 population)")
  .map(d => ({
    country: d["Data Source"],

  }))
)}

function _indicators(environmentData){return(
new Set(environmentData.map(d => d[""]))
)}

export default function define(runtime, observer) {
  const main = runtime.module();
  function toString() { return this.url; }
  const fileAttachments = new Map([
    ["environment-raw-2021@3.csv", {url: new URL("./files/7723ff80b688d12b555ee05a9976020b87a5020c1819a0c0f77f9a9ca90c4f2458c02fec2a33d4885a5effa42e335ae55f2880713bd8e2738648e7852c21d03a.csv", import.meta.url), mimeType: "text/csv", toString}]
  ]);
  main.builtin("FileAttachment", runtime.fileAttachments(name => fileAttachments.get(name)));
  main.variable(observer()).define(["md"], _1);
  main.variable(observer()).define(["md"], _2);
  main.variable(observer("environmentRaw20213")).define("environmentRaw20213", ["__query","FileAttachment","invalidation"], _environmentRaw20213);
  main.variable(observer("environmentData")).define("environmentData", ["FileAttachment"], _environmentData);
  main.variable(observer("filteredMortality")).define("filteredMortality", ["environmentData"], _filteredMortality);
  main.variable(observer("indicators")).define("indicators", ["environmentData"], _indicators);
  return main;
}
