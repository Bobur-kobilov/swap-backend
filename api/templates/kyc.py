MAIN_TEMPLATE = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>Hdac Tech.</title>
<meta content="text/html; charset=utf-8" http-equiv="Content-Type">
</head>
<body>
    <table align="left" cellpadding="0" cellspacing="0" style="table-layout: fixed" width="100%">
      <tbody>
        <tr>
          <td align="left">
            <table bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" style="table-layout: fixed" width="768">
              <tbody>
				<!-- header --> 
                <tr>
                   <td align="center" colspan="2" height="118" width="768"><img alt="HDAC-ATOLO 코인 스왑 Sub title Sub title  Sub title  Sub title Sub title Sub title" border="0" src="https://ap-swap.s3.ap-northeast-2.amazonaws.com/images/img_header.png" width="768" /></td>
                </tr>
				<!-- //header -->
				<!-- content -->
				<tr>
                  <td align="center" colspan="2">
					<div style="color:#333;font-family:'Noto Sans Korean';font-size:16px;text-align:left;width:580px;word-break:break-all;">
						제출하신 RIZON 지갑주소 <strong style="color:#00b1e9;font-size:16px;word-break:break-all;">{address}</strong>에 대한 인증이 정상적으로 완료됐습니다.<br><br>
						추후 HDAC-ATOLO 코인 스왑(교환)을 신청하실 때,<br>
						반드시 <strong>동일한 ATOLO 지갑주소(계좌)에 대한 복구단어</strong>를 입력하셔야<br>
						스왑을 받으실 수 있으니 이 점 유의 부탁 드립니다.<br><br>
						해당 KYC/AML 정보 등록에 대한 txid 는 다음과 같습니다.<br>
						<strong style="color:#00b1e9;font-size:16px;">{tx_hash}</strong><br><br>
					</div>
					<br>
					<img src="https://ap-swap.s3.ap-northeast-2.amazonaws.com/images/img_line.png" width="768" height="2" border="0" alt="라인"><br><br><br>
					<div style="color:#333;font-family:'Noto Sans Korean';font-size:16px;text-align:left;width:580px;word-break:break-all;">
						The KYC/AML certification regarding submitted<br>
						RIZON Wallet Address<strong style="color:#00b1e9;font-size:16px;">({address})</strong> has been completed successfully.<br><br>
						
						When you request for HDAC-ATOLO Coin Swap(Exchange),<br>
						please make sure that you type <strong>the same Recovery Words of<br>
						ATOLO Wallet Address(Account)</strong> to get the swap completed.<br><br>

						The txid of the KYC/AML certification information registration<br>
						is the following ID : <strong style="color:#00b1e9;font-size:16px;">{tx_hash}</strong>
					</div>
				  </td>
                </tr>
				<!-- //content -->
				</tbody>
            </table>
			<!-- footer -->
			<table bgcolor="ffffff" cellpadding="0" cellspacing="0" height="47" width="640">
				<tr>
                  <td align="center" colspan="2" height="80" width="768">&nbsp;</td>
                </tr>
              <tbody>
				<tr>
                  <td align="center" colspan="2" height="128" width="768"><a href="mailto:csteam@hdactech.com"><img alt="본 메일은 발신 전용으로 회신이 되지 않으며 당사가 지정한 수신자에 한해 발송되며, 어떠한 경우에도 당사의 허락없이 복사, 대여, 재배포될 수 없습니다. 문의사항은 csteam@hdactech.com으로 연락주시기 바랍니다." border="0" src="https://ap-swap.s3.ap-northeast-2.amazonaws.com/images/img_mail.png" width="768" /></a></td>
                </tr>
				<tr>
                 <td align="center" colspan="2" height="76" width="768"><img alt="Copyright &copy; 2020 Hdac Technology Co,. Ltd. All rights reserved" border="0" src="https://ap-swap.s3.ap-northeast-2.amazonaws.com/images/img_footer.png" width="768" /></td>
                </tr>
              </tbody>
            </table>
			<!-- footer -->
			</td>
        </tr>
      </tbody>
    </table>
  </body>
</html>
"""