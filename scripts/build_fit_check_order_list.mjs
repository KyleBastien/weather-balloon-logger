import fs from "node:fs/promises";
import { SpreadsheetFile, Workbook } from "@oai/artifact-tool";

const outDir = "outputs";
const outPath = `${outDir}/fit-check-order-list.xlsx`;
await fs.mkdir(outDir, { recursive: true });

const rows = [
  ["BUY NOW","Module","A1","DEV-13955","SparkFun OpenLog with Headers",1,1,"SparkFun","https://www.sparkfun.com/sparkfun-openlog-with-headers.html","Exact with-headers version"],
  ["BUY NOW","Module","A2","2123","Pololu S7V8F5 fixed 5 V regulator",1,1,"Pololu","https://www.pololu.com/product/2123","Use included straight header"],
  ["BUY NOW","Module","Host","LightAPRS-W 2.0 (+WSPR)","GPS/APRS/WSPR host module",1,1,"QRP Labs","https://www.qrp-labs.com/lightaprsw2.html","Exact 2.0 WSPR-capable module"],
  ["BUY NOW","Capacitor","C1,C5","C322C475K5R5TA","4.7 uF radial THT capacitor",2,4,"DigiKey","https://www.digikey.com/en/products/result?keywords=C322C475K5R5TA","Prototype spares included"],
  ["BUY NOW","Capacitor","C2-C4","C315C104K5R5TA","0.1 uF radial THT capacitor",3,10,"DigiKey","https://www.digikey.com/en/products/result?keywords=C315C104K5R5TA","Prototype spares included"],
  ["BUY NOW","LED","D1","WP710A10SGC","3 mm green THT LED",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=WP710A10SGC",""],
  ["BUY NOW","PCB connector","J1","S2B-PH-K-S(LF)(SN)","JST PH 2-pin side-entry THT header",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=S2B-PH-K-S%28LF%29%28SN%29","Battery input"],
  ["BUY NOW","Module header","J2","61301111121","1x11 2.54 mm straight THT header",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=61301111121","LightAPRS edge interface"],
  ["BUY NOW","RF connector","J3,J4","132134","50-ohm standard SMA female THT jack",2,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=132134","Not RP-SMA"],
  ["BUY NOW","PCB connector","J5","S2B-XH-A(LF)(SN)","JST XH 2-pin side-entry THT header",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=S2B-XH-A%28LF%29%28SN%29","Cutdown output"],
  ["BUY NOW","RF/module pin","J6,J7","61300111121","Single-pin 2.54 mm straight THT header",2,5,"DigiKey","https://www.digikey.com/en/products/result?keywords=61300111121","LightAPRS VHF/HF contacts"],
  ["BUY NOW","MOSFET","Q1","IRLZ44NPBF","Logic-level N-MOSFET, TO-220",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=IRLZ44NPBF",""],
  ["BUY NOW","Resistor","R1,R4","MFR-25FBF52-1K","1 kohm 1% 1/4 W axial",2,10,"DigiKey","https://www.digikey.com/en/products/detail/yageo/MFR-25FBF52-1K/13011",""],
  ["BUY NOW","Resistor","R2","MFR-25FBF52-100R","100 ohm 1% 1/4 W axial",1,5,"DigiKey","https://www.digikey.com/en/products/result?keywords=MFR-25FBF52-100R",""],
  ["BUY NOW","Resistor","R3","MFR-25FBF52-1M","1 Mohm 1% 1/4 W axial",1,5,"DigiKey","https://www.digikey.com/en/products/result?keywords=MFR-25FBF52-1M","Stock hold observed 2026-09-20; verify body before substitute"],
  ["BUY NOW","Switch","SW1","7101SYZQE","C&K SPDT toggle, solder terminals",1,1,"DigiKey","https://www.digikey.com/en/products/detail/c-k/SWITCH-7101SYZQE/25966","Do not substitute SYWQE"],
  ["BUY NOW","IC","U1","PCF8574N","I2C I/O expander, PDIP-16",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=PCF8574N",""],
  ["BUY NOW","IC","U2","TC4422AVPA","MOSFET gate driver, PDIP-8",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=TC4422AVPA",""],
  ["BUY NOW","Battery harness","Pack holder","BH3AAW","MPD 3xAA holder, 6-inch 24 AWG leads",1,1,"DigiKey","https://www.digikey.com/en/products/detail/mpd-memory-protection-devices/BH3AAW/32050","Off-board; pulse/cold qualification required"],
  ["BUY NOW","Battery harness","J1 mate","PHR-2","JST PH 2-position receptacle housing",1,2,"DigiKey","https://www.digikey.com/en/products/detail/jst-sales-america-inc/PHR-2/608607","Housing only"],
  ["BUY NOW","Battery harness","J1 leads","ASPHSPH24K152","24 AWG 6-inch pre-crimp socket-to-socket lead",2,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=ASPHSPH24K152","Cut in half; permanently mark polarity"],
  ["BUY NOW","Cutdown harness","J5 mate","XHP-2","JST XH 2-position receptacle housing",1,2,"DigiKey","https://www.digikey.com/en/products/result?keywords=XHP-2","Housing only"],
  ["BUY NOW","Cutdown harness","J5 leads","ASXHSXH22K152","22 AWG 6-inch pre-crimp socket-to-socket lead",2,2,"DigiKey","https://www.digikey.com/en/products/detail/jst-sales-america-inc/ASXHSXH22K152/6684931","Cut in half; identify PACK+ and FET-"],
  ["BUY NOW","Power","Flight/test cells","Energizer L91","AA lithium primary cell",3,6,"Authorized retailer","https://data.energizer.com/pdfs/l91.pdf","Two matched 3-cell sets"],
  ["BUY NOW","Storage","OpenLog media","microSDHC <=32 GB","FAT32 microSD card",1,2,"Reputable retailer","https://www.sparkfun.com/sparkfun-openlog-with-headers.html","One spare"],
  ["BUY NOW","Mechanical fit tool","Module spacing","M2 nylon hardware assortment","M2 spacers, screws, nuts",4,1,"Local supplier","","Fit tool only; final height held"],
  ["BUY NOW","Consumable","Harness splices","22-24 AWG adhesive heat-shrink","Adhesive-lined heat-shrink assortment",4,1,"Local supplier","","Copper splice insulation only"],
  ["HOLD","Fabrication","Carrier PCB","Bare PCB","Fabricated weather-balloon-logger carrier",1,0,"PCB fabricator","","Order only after exact-parts 1:1 fit gate passes"],
  ["HOLD","RF system","APRS","TBD","144-146 MHz antenna and 50-ohm SMA-male cable",1,0,"TBD","","Needs payload geometry, cable length, VSWR"],
  ["HOLD","RF system","WSPR","TBD","Band-specific LPF, antenna, and SMA-male cable",1,0,"TBD","","Band is not released; onboard HF LPF absent"],
  ["HOLD","Cutdown","Burn element","TBD Nichrome 80","Nichrome gauge and active length",1,0,"TBD","","Bench-select for 3.0-5.4 V, <=2 A, <=30 s"],
  ["HOLD","Cutdown","Burn-wire joint","TBD crimp sleeve","Nichrome-to-copper mechanical splice",2,0,"TBD","","Size after wire selection; do not rely on solder"],
  ["HOLD","Mechanical","Flight module spacers","TBD M2 standoffs","Final LightAPRS mounting hardware",4,0,"TBD","","Measure physical stack and hole centers first"],
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
  ["Prepared", "2026-09-20"],
  ["Scope", "One complete carrier fit check plus practical prototype spares"],
  ["Buy-now line items", null],
  ["Held line items", null],
  ["Required populated PCB refs", 23],
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
  ["2", "Use pre-crimp leads", "Avoids specialized JST production tooling for the prototype.", null, null, null],
  ["3", "Observe J1 limit", "JST-PH is at the 2 A cutdown-current edge; pulse/cold test the finished harness.", null, null, null],
  ["4", "Keep flight-critical holds", "Antenna, LPF, nichrome, sleeves, and final spacers need physical/test inputs.", null, null, null],
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
holds.getRange("A2:D7").values = [
  ["Bare PCB fabrication","Exact-parts fit gate precedes fabrication","Place all board parts and LightAPRS on the 1:1 PDF; verify scale, bodies, holes, connector access, and cable bends","OPEN"],
  ["APRS antenna/cable","Payload geometry and cable length not released","Select enclosure layout and verify 50-ohm SMA-male mate plus VHF VSWR","OPEN"],
  ["WSPR LPF/antenna/cable","Band not released; module has no onboard HF LPF","Select authorized band; design filter/antenna; verify match and harmonics","OPEN"],
  ["Nichrome wire","Gauge/length set resistance and current","Cold bench test from 3.0-5.4 V within <=2 A and <=30 s","OPEN"],
  ["Nichrome sleeves","Sleeve size follows final wire diameters","Choose compatible mechanical crimps; prove pull strength and contact heating","OPEN"],
  ["Final M2 spacers","Physical module stack-up remains unmeasured","Measure hole centers and clearance; select exact spacer length/material","OPEN"],
];
holds.getRange("A1:D1").format = { fill: navy, font: { name: font, bold: true, color: "#FFFFFF" }, wrapText: true };
holds.getRange("A2:D7").format = { font: { name: font }, wrapText: true, verticalAlignment: "top", borders: { preset: "all", style: "thin", color: "#D9D9D9" } };
holds.getRange("D2:D7").format = { fill: amber, font: { name: font, bold: true, color: "#9C6500" }, horizontalAlignment: "center" };
holds.getRange("A1:D1").format.rowHeight = 28;
holds.getRange("A2:D7").format.rowHeight = 58;
[24,42,62,14].forEach((w,i)=>holds.getRangeByIndexes(0,i,7,1).format.columnWidth=w);
holds.freezePanes.freezeRows(1);
const holdTable = holds.tables.add("A1:D7", true, "HoldClosureTable");
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
