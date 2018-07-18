<?php

$start_time = time();
echo "processing 2 csv file filtering using php\n";
echo "start time: {$start_time}\n";
$send_file_csv = 'send-list.csv';
$block_file_csv = 'block-list.csv';
$filter_file_csv = 'filter-list.csv';
$send_lines = file($send_file_csv, FILE_IGNORE_NEW_LINES);
$block_lines = file($block_file_csv, FILE_IGNORE_NEW_LINES);
$step1_time = time();
$elapsed_time = (float)($step1_time - $start_time);
echo "Done appending 2 source csvs into separate arrays in {$elapsed_time} seconds.\n";

$filter_lines = array_diff($send_lines, $block_lines);
$step2_time = time();
$elapsed_time = (float)($step2_time - $step1_time);
echo "Done getting difference between 2 csvs in {$elapsed_time} seconds.\n";

$filter_file = fopen($filter_file_csv,"w");
foreach (array_unique($filter_lines) as $line){
	fputcsv($filter_file,explode(',',$line));
}
$step3_time = time();
$elapsed_time = (float)($step3_time - $step2_time);
echo "Done removing duplicates and writing results to new csv in {$elapsed_time} seconds.\n";

fclose($filter_file);
unset($send_lines);
unset($block_lines);
unset($filter_lines);
$end_time = time();
$execution_time = (float)($end_time - $start_time);
echo "Total Execution time: {$execution_time} seconds\n";
?>