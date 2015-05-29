op_profile_min <- read.csv("~/Desktop/2042_Labs/OpenPayments/cms-merge/data/op_profile_min.csv")
npi_data_min <- read.csv("~/Desktop/2042_Labs/OpenPayments/cms-merge/data/npi_data_min.csv")

npi_docs_only <- npi_data_min[npi_data_min$LastName != "",]

merged <- merge(op_profile_min, npi_docs_only, by=c("LastName","FirstName","MiddleInitial","ZipCode5"))
merged$NPI <- merged$NPI.y
merged$OpProfileId <- merged$OpProfileID.x
merged2 <- merged[,-c(5,6,7,8)]

write.csv(merged, file="initial_merge.csv", row.names=FALSE, quote=FALSE)

op_profile_missing <- op_profile_min[!(op_profile_min$OpProfileID %in% merged$OpProfileId),]
prof_dup_idx <- duplicated(op_profile_min[,-6])

profile_dups <- op_profile_min[prof_dup_idx,]

write.csv(profile_dups, file="op_profile_duplicates.csv", row.names=FALSE, quote=FALSE)

merged_npi_dup_idx <- duplicated(merged[,-5])
merged_npi_dups <- merged[merged_npi_dup_idx,]

write.csv(merged_npi_dups, file="merged_npi_duplicates.csv", row.names=FALSE, quote=FALSE)


