p.threshold <- c(0.001,0.05,0.1,0.2,0.3,0.4,0.5)
# Read in the phenotype file 
phenotype <- read.table("/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_pheno_data.txt", header=T)
# Read in the PCs
pcs <- read.table("/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_targetData_pca.eigenvec", header=F)
# The default output from plink does not include a header
# To make things simple, we will add the appropriate headers
# (1:6 because there are 6 PCs)
#colnames(phenotype) <- c("FID", "IID", "Phenotype")
colnames(pcs) <- c("FID", "IID", paste0("PC",1:6)) 
# Read in the covariates (here, it is sex)
covariate <- read.table("/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_cov_data.txt", header=T)
#colnames(covariate) <- c("FID", "IID", "Age", "Gender")
# Now merge the files
pheno <- merge(merge(phenotype, covariate, by=c("FID", "IID")), pcs, by=c("FID","IID"))
# We can then calculate the null model (model with PRS) using a linear regression 
# (as height is quantitative)
null.model <- glm(Phenotype~., data=pheno[,!colnames(pheno)%in%c("FID","IID")], family = "binomial")
# And the R2 of the null model is 
#null.r2 <- summary(null.model)$r.squared
prs.result <- NULL
for(i in p.threshold){
    # Go through each p-value threshold
    prs <- read.table(paste0("/home/iHiO10009/yuching/data/2.PRS/case_ageMatchControl_PRS/ageMatch_PRS.",i,".profile"), header=T)
    # Merge the prs with the phenotype matrix
    # We only want the FID, IID and PRS from the PRS file, therefore we only select the 
    # relevant columns
    pheno.prs <- merge(pheno, prs[,c("FID","IID", "SCORE")], by=c("FID", "IID"))
    # Now perform a linear regression on Height with PRS and the covariates
    # ignoring the FID and IID from our model
    model <- glm(Phenotype~., data=pheno.prs[,!colnames(pheno.prs)%in%c("FID","IID")])
    # model R2 is obtained as
    # Not sure if the below is the right way to calculate R2
    prs.r2 <- 1-logLik(model)/logLik(null.model)
    #print(summary(model)) 
    #print(model.r2 <- summary(model)$r.squared)
    # R2 of PRS is simply calculated as the model R2 minus the null R2
    #prs.r2 <- model.r2-null.r2
    # We can also obtain the coeffcient and p-value of association of PRS as follow
    prs.coef <- summary(model)$coeff["SCORE",]
    prs.beta <- as.numeric(prs.coef[1])
    prs.se <- as.numeric(prs.coef[2])
    prs.p <- as.numeric(prs.coef[4])
    # We can then store the results
    prs.result <- rbind(prs.result, data.frame(Threshold=i, R2=prs.r2, P=prs.p, BETA=prs.beta,SE=prs.se))
}
# Best result is:
prs.result[which.max(prs.result$R2),]
