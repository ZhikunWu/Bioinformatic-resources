#!/usr/bin/perl
use strict;
use warnings;

##### usage: perl chip_geno_filter.pl input filter_output stastics_output
##### Author: Wu Zhikun
##### Time: 2016.09.19

open my $in, "< $ARGV[0]";
##the input format:  the second and third columns are two parents, others are offsprings.
## Name	108.GType	109.GType	1.GType	2.GType
## Bn-A01-p10000230	BB	BB	BB	BB

open my $out1, "> $ARGV[1]";  ###the output for the marker after filtering with the above parameters
open my $out2, "> $ARGV[2]";  ###the output for the stastics of filtering

########parameters:
my $heri_threshold = 0.2;
my $missing_threshold = 0.2;
my $seg_distortion_threshold = 0.1;
#################

my $header = <$in>;
chomp($header);
my @headers = split("\t",$header);

my @geno;
while (my $line = <$in>){
	chomp($line);
	my @lines = split ("\t",$line);
	push (@geno,[@lines]);
	
}
close $in;

my %taxa_geno; 
my @new_headers;

my @temp;
for (my $j = 1; $j <= $#{$geno[0]}; $j++){
	my ($AA,$BB,$AB,$NC);
	my $heri;	
	for (my $i = 0; $i <= $#geno; $i++){
		push (@temp,$geno[$i][$j]); 
		if($geno[$i][$j] eq "AA"){
			$AA++;
		}elsif($geno[$i][$j] eq "BB"){
			$BB++;
		}elsif($geno[$i][$j] eq "AB"){
			$AB++;
		}elsif($geno[$i][$j] eq "NC"){
			$NC++;
		}else{
			$NC++;
		}
	}
	###### calculate the heritability and filter the lines based on the threshold
	my $NON_NC = $AA + $AB + $BB;
	if ($NON_NC eq "0"){
		$heri = 1;
	}else {
		$heri = $AB / $NON_NC; 
	}
	
	if ($heri <= $heri_threshold){
	
		@{$taxa_geno{$headers[$j]}} = @temp;
		undef @temp;
		push (@new_headers, $headers[$j]);
	}
}


my @markers;
my %marker_geno;
for(my $p = 0; $p <= $#geno; $p++){
	push (@markers,$geno[$p][0]);
}

########construct the hash with marker and the genotype after filtering the taxas with high heritability
my @after_heri_geno;
if ($#markers eq $#{$taxa_geno{$new_headers[0]}} ){
	my @temp2;
	for (my $ii = 0; $ii <= $#markers; $ii++){
		for (my $jj = 0; $jj <= $#new_headers; $jj++){
			push (@temp2,${$taxa_geno{$new_headers[$jj]}}[$ii]);
		}
		@{$marker_geno{$markers[$ii]}} = @temp2;
		undef @temp2;
	}
}else{
	print "ERROR! The numbers of markers and the genotype after filtering are not equal !"."\n";
	print "Check it !";
}


print $out1 "Name"."\t".join("\t",@new_headers)."\n";

my ($bi_A_B,$or_NC,$M,$p1,$p2);
my @dis_markers;
my $dis_num = 0;
foreach my $h_taxa(sort keys %marker_geno){
	my @h_geno = @{$marker_geno{$h_taxa}};
	$p1 = $h_geno[0];
	$p2 = $h_geno[1];
	if( ($p1 eq "AA" && $p2 eq "AA") || ($p1 eq "BB" && $p2 eq "BB") || ($p1 eq "AB" && $p2 eq "AB") ){
		$bi_A_B++;
	}elsif($p1 eq "NC" || $p2 eq "NC"){
		$or_NC++;
	}elsif( ($p1 ne $p2 )){  ###do not delete the marker with AB for one parent
		my @temp3;
		my $A = 0;
		my $B = 0;
		my $U = 0;
		for (my $k = 2; $k <= $#h_geno; $k++){ ##the genotype same to first parent was coded as "A", and the other as "B" 
			if($p1 eq $h_geno[$k]){
				$A++;
				push (@temp3,"A");
			}elsif($p2 eq $h_geno[$k]){
				$B++;
				push (@temp3,"B");
			}else{
				$U++;
				push (@temp3,"U");
			}
		}
		my $missing;
		if((scalar(@h_geno)-2) eq 0){
			$missing = 1;
		}else{
			$missing = $U / (scalar(@h_geno)-2);
		}
		
		if ($missing <= $missing_threshold){
			my $new_geno = join("\t","A","B",@temp3);
			print $out1 $h_taxa."\t".$new_geno."\n";
		}else{
			$M++;
		}
		undef @temp3;
		my $distortion;
		if(($A + $B) ne 0){
			$distortion = $A/($A + $B); 
		}
		if ($distortion < $seg_distortion_threshold ||  $distortion > (1-$seg_distortion_threshold)){
			$dis_num++;
			push (@dis_markers,$h_taxa);
		}
	}
	
}

my $useful_num = $#geno + 1  - $bi_A_B - $or_NC - $M; ##don't exclude the segregation distortion markers at now

print $out2 "Useful markers after filtering "."\t".$useful_num."\n";
print $out2 "Both AA, BB or AB for parents  "."\t".$bi_A_B."\n";
print $out2 "Any one NC for parents         "."\t".$or_NC."\n";
print $out2 "Missing above the threshold    "."\t".$M."\n";
print $out2 "Segregation distortion rate    "."\t".$dis_num."\n";
print $out2 "Segregation distortion markers:"."\t".join("\t",@dis_markers)."\n";


 








