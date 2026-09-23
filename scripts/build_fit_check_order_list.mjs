import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outDir = "outputs";
const outPath = `${outDir}/fit-check-order-list.xlsx`;
await fs.mkdir(outDir, { recursive: true });

const rows = [
  ["BUY NOW","Module","A1","DEV-13955","SparkFun OpenLog with Headers",1,1,"SparkFun","https://www.sparkfun.com/sparkfun-openlog-with-headers.html","Exact with-headers version"],
  ["BUY NOW","Module","Host","LightHABTracker 1.0","GPS/APRS/WSPR tracker with 3xAA holder and two pyro outputs",1,1,"QRP Labs","https://shop.qrp-labs.com/aprs/LightHABTracker","Measure the purchased board before fabricating the carrier"],
  ["BUY NOW","Capacitor","C1","C322C475K5R5TA","4.7 uF radial THT capacitor",1,3,"DigiKey","https://www.digikey.com/en/products/result?keywords=C322C475K5R5TA","Prototype spares included"],
  ["BUY NOW","Capacitor","C2","C315C104K5R5TA","0.1 uF radial THT capacitor",1,5,"DigiKey","https://www.digikey.com/en/products/result?keywords=C315C104K5R5TA","Prototype spares included"],
  ["BUY NOW","LED","D1","WP710A10SGC","3 mm green THT LED",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=WP710A10SGC",""],
  ["BUY NOW","PCB connector","J5","S2B-XH-A(LF)(SN)","JST XH 2-pin side-entry THT header",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=S2B-XH-A%28LF%29%28SN%29","Cutdown output"],
  ["BUY NOW","Resistor","R1,R4","MFR-25FBF52-1K","1 kohm 1% 1/4 W axial",2,10,"DigiKey","https://www.digikey.com/en/products/detail/yageo/MFR-25FBF52-1K/13011",""],
  ["BUY NOW","Resistor","R2","MFR-25FBF52-100K","100 kohm 1% 1/4 W axial",1,5,"DigiKey","https://www.digikey.com/en/products/result?keywords=MFR-25FBF52-100K","LED reset-default-off pull-up"],
  ["BUY NOW","Cutdown harness","J5 mate","XHP-2","JST XH 2-position receptacle housing",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=XHP-2","Housing only"],
  ["BUY NOW","Cutdown harness","J5 leads","ASXHSXH22K152","22 AWG 6-inch pre-crimp socket-to-socket lead",2,2,"DigiKey","https://www.digikey.com/en/products/detail/jst-sales-america-inc/ASXHSXH22K152/6684931","Cut in half; identify OUT1 and GND"],
  ["BUY NOW","Power","Flight/test cells","Energizer L91","AA lithium primary cell",3,6,"Authorized retailer","https://data.energizer.com/pdfs/l91.pdf","Two matched 3-cell sets"],
  ["BUY NOW","Storage","OpenLog media","microSDHC <=32 GB","FAT32 microSD card",1,2,"Reputable retailer","https://www.sparkfun.com/sparkfun-openlog-with-headers.html","One spare"],
  ["BUY NOW","Mechanical fit tool","Module spacing","M2/M2.5 nylon hardware assortment","Spacers, screws, and nuts",4,1,"Local supplier","","Fit tool only; final diameter and height held"],
  ["HOLD","Module interface","J2","TBD after measurement","Nine-position signal solder interface",1,0,"TBD","","Verify actual row pitch, location, and installed header direction"],
  ["HOLD","Module interface","J3","TBD after measurement","Two-position OUT1/GND solder interface",1,0,"TBD","","Measure pad pitch, hole size, and mating method on LightHAB"],
  ["HOLD","Fabrication","Carrier PCB","Bare PCB","Fabricated weather-balloon-logger carrier",1,0,"PCB fabricator","","Order only after exact-parts 1:1 fit gate passes"],
  ["HOLD","RF system","Antennas/cables","TBD","APRS and WSPR antennas/cables for onboard SMA ports",2,0,"TBD","","Needs selected bands, payload geometry, cable length, and VSWR"],
  ["HOLD","Cutdown","Burn element","TBD Nichrome 80","Nichrome gauge and active length",1,0,"TBD","","Bench-select against verified LightHAB OUT1 rating and cold battery behavior"],
  ["HOLD","Cutdown","Burn-wire joint","TBD crimp sleeve","Nichrome-to-copper mechanical splice",2,0,"TBD","","Size after wire selection; do not rely on solder"],
  ["HOLD","Mechanical","Flight module spacers","TBD after measurement","Final LightHAB mounting hardware",4,0,"TBD","","Measure physical stack, holes, battery holder, USB, and SMA clearance first"],
];

const wb = Workbook.create();
const summary = wb.worksheets.add("Summary");
const order = wb.worksheets.add("Order List");
const holds = wb.worksheets.add("Hold Closure");
const navy = "#17365D", blue = "#D9EAF7", green = "#E2F0D9", amber = "#FFF2CC", red = "#F4CCCC", gray = "#E7E6E6";
const font = "Arial";

summary.showGridLines = false;
summary.mergeCells("A1:F1");
summary.getRange("A1").values = [["Weather Balloon Logger - Fit-Check Order"]];
summary.getRange("A1:F1").format = { fill: navy, font: { name: font, size: 18, bold: true, color: "#FFFFFF" }, verticalAlignment: "center" };
summary.getRange("A1:F1").format.rowHeight = 32;
summary.getRange("A3:B8").values = [
  ["Prepared", "2026-09-22"],
  ["Scope", "One complete carrier fit check plus practical prototype spares"],
  ["Buy-now line items", null],
  ["Held line items", null],
  ["Required populated PCB refs", 10],
  ["Primary gate", "Do not fabricate until the 1:1 exact-parts fit check passes"],
];
summary.getRange("B5").formulas = [[`=COUNTIF('Order List'!$A$2:$A$${rows.length+1},"BUY NOW")`]];
summary.getRange("B6").formulas = [[`=COUNTIF('Order List'!$A$2:$A$${rows.length+1},"HOLD")`]];
summary.getRange("A3:A8").format = { fill: blue, font: { name: font, bold: true, color: navy }, borders: { preset: "all", style: "thin", color: "#B4C6E7" } };
summary.getRange("B3:B8").format = { font: { name: font }, wrapText: true, borders: { preset: "all", style: "thin", color: "#B4C6E7" } };
summary.getRange("A10:F10").merge();
summary.getRange("A10").values = [["Ordering rules"]];
summary.getRange("A10:F10").format = { fill: navy, font: { name: font, bold: true, color: "#FFFFFF" } };
summary.getRange("A11:F15").values = [
  ["1", "Buy exact MPNs for fit", "Substitutes can change body, lead pitch, or connector envelope.", null, null, null],
  ["2", "Measure LightHAB first", "J2/J3 and all four mounting holes remain provisional until the purchased tracker is measured.", null, null, null],
  ["3", "Use pre-crimp J5 leads", "Avoids specialized JST production tooling for the prototype cutdown harness.", null, null, null],
  ["4", "Keep flight-critical holds", "Interfaces, antennas, nichrome, sleeves, and final spacers need physical or test inputs.", null, null, null],
  ["5", "Recheck checkout", "Stock, price, tariffs, and authorized-distributor status can change.", null, null, null],
];
summary.getRange("A11:F15").format = { font: { name: font }, wrapText: true, borders: { preset: "all", style: "thin", color: "#D9D9D9" } };
summary.getRange("A3:A15").format.columnWidth = 22;
summary.getRange("B3:B15").format.columnWidth = 44;
summary.getRange("C3:C15").format.columnWidth = 48;
summary.getRange("D3:F15").format.columnWidth = 12;
summary.getRange("A3:F15").format.autofitRows();
summary.freezePanes.freezeRows(1);

order.showGridLines = false;
const headers = ["Status","Category","Ref / Use","Manufacturer Part","Description","Need","Order","Source","Order / source link","Fit-check notes"];
order.getRange("A1:J1").values = [headers];
order.getRange(`A2:J${rows.length+1}`).values = rows;
order.getRange("A1:J1").format = { fill: navy, font: { name: font, bold: true, color: "#FFFFFF" }, wrapText: true, verticalAlignment: "center", borders: { preset: "all", style: "thin", color: "#FFFFFF" } };
order.getRange(`A2:J${rows.length+1}`).format = { font: { name: font, size: 10 }, wrapText: true, verticalAlignment: "top", borders: { preset: "all", style: "thin", color: "#D9D9D9" } };
order.getRange(`A2:A${rows.length+1}`).conditionalFormats.add("containsText", { text: "BUY NOW", format: { fill: green, font: { bold: true, color: "#375623" } } });
order.getRange(`A2:A${rows.length+1}`).conditionalFormats.add("containsText", { text: "HOLD", format: { fill: red, font: { bold: true, color: "#9C0006" } } });
order.getRange(`F2:G${rows.length+1}`).format.numberFormat = "0";
order.getRange(`A1:J${rows.length+1}`).format.autofitRows();
const widths = [12,18,16,28,36,8,8,18,52,48];
for (let i = 0; i < widths.length; i++) order.getRangeByIndexes(0,i,rows.length+1,1).format.columnWidth = widths[i];
order.freezePanes.freezeRows(1);
order.freezePanes.freezeColumns(1);
const tbl = order.tables.add(`A1:J${rows.length+1}`, true, "FitCheckOrderTable");
tbl.style = "TableStyleMedium2";
tbl.showFilterButton = true;

holds.showGridLines = false;
holds.getRange("A1:D1").values = [["Held item","Reason","Close the hold by","Release state"]];
holds.getRange("A2:D9").values = [
  ["LightHAB J2/J3 interfaces","Vendor mechanical geometry is not published","Measure pitch, hole diameter, row location, orientation, and solder access on the purchased board","OPEN"],
  ["LightHAB mounting holes","Provisional carrier coordinates are not authoritative","Measure all centers and diameters; update H1-H4 and the module outline","OPEN"],
  ["Bare PCB fabrication","Measured-module fit gate precedes fabrication","Update CAD, print the 1:1 PDF, and verify all exact parts plus USB/SMA/battery clearances","OPEN"],
  ["APRS/WSPR antennas and cables","Bands and payload geometry are not released","Select bands and enclosure layout; verify SMA mating, cable routing, match, and harmonics","OPEN"],
  ["Nichrome wire","Gauge/length set resistance and current","Verify LightHAB OUT1 rating, then cold-test the selected wire and pulse duration","OPEN"],
  ["Nichrome sleeves","Sleeve size follows final wire diameters","Choose compatible mechanical crimps; prove pull strength and contact heating","OPEN"],
  ["Final mounting hardware","Physical module stack-up remains unmeasured","Measure hole diameter, board spacing, battery holder, USB, SMA, and underside clearance","OPEN"],
  ["LightHAB 3V3/OUT1 behavior","3V3 rail capacity and pyro current rating are unverified","Stress the 3V3 rail with OpenLog and radio activity; qualify OUT1 with an inert load before attaching nichrome","OPEN"],
];
holds.getRange("A1:D1").format = { fill: navy, font: { name: font, bold: true, color: "#FFFFFF" }, wrapText: true };
holds.getRange("A2:D9").format = { font: { name: font }, wrapText: true, verticalAlignment: "top", borders: { preset: "all", style: "thin", color: "#D9D9D9" } };
holds.getRange("D2:D9").format = { fill: amber, font: { name: font, bold: true, color: "#9C6500" }, horizontalAlignment: "center" };
holds.getRange("A1:D1").format.rowHeight = 28;
holds.getRange("A2:D9").format.rowHeight = 58;
[24,42,62,14].forEach((w,i)=>holds.getRangeByIndexes(0,i,9,1).format.columnWidth=w);
holds.freezePanes.freezeRows(1);
const holdTable = holds.tables.add("A1:D9", true, "HoldClosureTable");
holdTable.style = "TableStyleMedium2";

wb.recalculate();
const inspect = await wb.inspect({ kind: "sheet,formula", maxChars: 5000, tableMaxRows: 2, tableMaxCols: 4 });
console.log(inspect.ndjson);
const errorScan = await wb.inspect({
  kind: "match",
  searchTerm: "#REF!|#DIV/0!|#VALUE!|#NAME\\?|#N/A|#NUM!|#NULL!|#SPILL!|#CALC!",
  options: { useRegex: true, maxResults: 300 },
  maxChars: 5000,
});
console.log(errorScan.ndjson);
for (const name of ["Summary","Order List","Hold Closure"]) {
  const preview = await wb.render({ sheetName: name, autoCrop: "all", scale: 1, format: "png" });
  await fs.writeFile(`${outDir}/fit-check-order-list-${name.toLowerCase().replaceAll(" ","-")}.png`, new Uint8Array(await preview.arrayBuffer()));
}
const xlsx = await SpreadsheetFile.exportXlsx(wb);
await xlsx.save(outPath);
console.log(`Saved ${outPath}`);
