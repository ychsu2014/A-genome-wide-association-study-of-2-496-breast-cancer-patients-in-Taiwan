input_file = "/home/iHiO10009/Dataset/dbSNP/GCF_000001405.25"
#input_file = "/home/iHiO10009/yuching/data/dbSNP/test.vcf"

import vcf

vcf_reader = vcf.Reader(open(input_file))
for i in range(1,10):
    num_str = str(i)
    out_file = "/home/iHiO10009/yuching/data/dbSNP/NC_00000" + num_str + ".vcf"
    exec("vcf_writer" + num_str + " = vcf.Writer(open(out_file, 'w'), vcf_reader)")

for i in range(10,25):
    num_str = str(i)
    out_file = "/home/iHiO10009/yuching/data/dbSNP/NC_0000" + num_str + ".vcf"
    exec("vcf_writer" + num_str + " = vcf.Writer(open(out_file, 'w'), vcf_reader)")

count = 0
for record in vcf_reader:
    count += 1
    if count % 100000000 == 0:
        print(count)
    chrom = record.CHROM
    #print(type(chrom))  #str
    if "NC_000001" in chrom:
        vcf_writer1.write_record(record)
    elif "NC_000002" in chrom:
        vcf_writer2.write_record(record)
    elif "NC_000003" in chrom:
        vcf_writer3.write_record(record)
    elif "NC_000004" in chrom:
        vcf_writer4.write_record(record)
    elif "NC_000005" in chrom:
        vcf_writer5.write_record(record)
    elif "NC_000006" in chrom:
        vcf_writer6.write_record(record)
    elif "NC_000007" in chrom:
        vcf_writer7.write_record(record)
    elif "NC_000008" in chrom:
        vcf_writer8.write_record(record)
    elif "NC_000009" in chrom:
        vcf_writer9.write_record(record)
    elif "NC_000010" in chrom:
        vcf_writer10.write_record(record)
    elif "NC_000011" in chrom:
        vcf_writer11.write_record(record)
    elif "NC_000012" in chrom:
        vcf_writer12.write_record(record)
    elif "NC_000013" in chrom:
        vcf_writer13.write_record(record)
    elif "NC_000014" in chrom:
        vcf_writer14.write_record(record)
    elif "NC_000015" in chrom:
        vcf_writer15.write_record(record)
    elif "NC_000016" in chrom:
        vcf_writer16.write_record(record)
    elif "NC_000017" in chrom:
        vcf_writer17.write_record(record)
    elif "NC_000018" in chrom:
        vcf_writer18.write_record(record)
    elif "NC_000019" in chrom:
        vcf_writer19.write_record(record)
    elif "NC_000020" in chrom:
        vcf_writer20.write_record(record)
    elif "NC_000021" in chrom:
        vcf_writer21.write_record(record)
    elif "NC_000022" in chrom:
        vcf_writer22.write_record(record)
    elif "NC_000023" in chrom:
        vcf_writer23.write_record(record)
    elif "NC_000024" in chrom:
        vcf_writer24.write_record(record)

for i in range(1,25):
    exec("vcf_writer" + str(i) + ".close()")

#parseChrom(input_file, "NC_000001")
#parseChrom(input_file, "NC_000002")
#parseChrom(input_file, "NC_000003")
#parseChrom(input_file, "NC_000004")
#parseChrom(input_file, "NC_000005")
#parseChrom(input_file, "NC_000006")
#parseChrom(input_file, "NC_000007")
#parseChrom(input_file, "NC_000008")
#parseChrom(input_file, "NC_000009")
#parseChrom(input_file, "NC_000010")
#parseChrom(input_file, "NC_000011")
#parseChrom(input_file, "NC_000012")
#parseChrom(input_file, "NC_000013")
#parseChrom(input_file, "NC_000014")
#parseChrom(input_file, "NC_000015")
#parseChrom(input_file, "NC_000016")
#parseChrom(input_file, "NC_000017")
#parseChrom(input_file, "NC_000018")
#parseChrom(input_file, "NC_000019")
#parseChrom(input_file, "NC_000020")
#parseChrom(input_file, "NC_000021")
#parseChrom(input_file, "NC_000022")
#parseChrom(input_file, "NC_000023")
#parseChrom(input_file, "NC_000024")
