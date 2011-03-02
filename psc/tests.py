import unittest
from rapidsms.tests.scripted import TestScript

class TestPSC(TestScript):
    fixtures = ['observers', 'unknown_rcs']

    def setUp(self):
        super(TestPSC, self).setUp()

    def testVRChecklist(self):
        self.assertInteraction("""
          1234 > psc111111vr12rc999
          1234 < Observer ID not found. Please resend with valid PSC. You sent: PSC111111VR12RC999
          1234 > PSC366001VRRC113A2B1C2D4E5F2G2
          1234 < Invalid message:"PSC366001VRRC113A2B1C2D4E5F2G2". Please resend!
          1234 > PSC366001VR03RC113A2B3C2D4E5F2G3
          1234 < Invalid response(s) for question(s): "B, G". You sent: PSC366001VR03RC113A2B3C2D4E5F2G3
          1234 > PSC366001VR03RC11A2B1C2D4E5F2G2
          1234 < Invalid message:"PSC366001VR03RC11A2B1C2D4E5F2G2". Please resend!
          1234 > PSC712001VR22RC005A2B1C2D4E24FG2
          1234 < Invalid responses for the checklist code: "FG". You sent: PSC712001VR22RC005A2B1C2D4E24FG2
          1234 > PSC172001VR22GA639!5E
          1234 < Invalid message:"PSC172001VR22GA639!5E". Please resend!
          1234 > PSC172001VR22GA639!
          1234 < Invalid message:"PSC172001VR22GA639!". Please resend!
          1234 > PSC786001VR20RC157A3B1C2D4E5FN0NG2
          1234 < Invalid responses for the checklist code: "NG, FN". You sent: PSC786001VR20RC157A3B1C2D4E5FN0NG2
          1234 > PSC510001DY20RC137A1B1C2D4E234F0G1
          1234 < Invalid message:"PSC510001DY20RC137A1B1C2D4E234F0G1". Please resend!
          1234 > PSC827001UR20RC187A2B1C3D4E5F0G2GUA
          1234 < Invalid message:"PSC827001UR20RC187A2B1C3D4E5F0G2GUA". Please resend!
          1234 > PSC9650001VR20RC0KERE2007A3B1C2D4E5F0G2
          1234 < Invalid message:"PSC9650001VR20RC0KERE2007A3B1C2D4E5F0G2". Please resend!
          1234 > PSC510001VR20RC137A1B1C2D4E234F0G1
          1234 < VR Checklist report accepted! You sent: PSC510001VR20RC137A1B1C2D4E234F0G1
          1234 > PSC510001VR20RC137A1B1C12D4E234F70G1
          1234 < Invalid response(s) for question(s): "C, F". You sent: PSC510001VR20RC137A1B1C12D4E234F70G1
          1234 > psc584001vr20rc103h1j1k2m1n5p4q5r5s1t2u2v2w2x2y4z420aa420
          1234 < VR Checklist report accepted! You sent: PSC584001VR20RC103H1J1K2M1N5P4Q5R5S1T2U2V2W2X2Y4Z420AA420
          1234 > psc319002vr20rc009ang/galadimaa1b1c31e2f9g3
          1234 < Invalid responses for the checklist code: "AD, MAA, ANGGA". Invalid response(s) for question(s): "C, G". You sent: PSC319002VR20RC009ANGGA1AD1MAA1B1C31E2F9G3
          1234 > PSC319002VR15RC139A1B1C3D45F8G12NDTEXTANGGA1AD1MA11A1B1C3D4E5F8G13RDTEXTGH1J1K2M5N5P5Q5R5S1T1U1V1W2X2Y999Z9999AA9999
          1234 < Invalid responses for the checklist code: "RDTEXTGH, NDTEXTANGGA, AD, MA". Invalid response(s) for question(s): "G". You sent: PSC319002VR15RC139A1B1C3D45F8G12NDTEXTANGGA1AD1MA11A1B1C3D4E5F8G13RDTEXTGH1J1K2M5N5P5Q5R5S1T1U1V1W2X2Y999Z9999AA9999
          1234 > PSC941001UR15RC105H1J1K1M5N5P5Q5R5S1T2U2V1WCX2Y17Z17AA17@everythin went well
          1234 < Invalid message:"PSC941001UR15RC105H1J1K1M5N5P5Q5R5S1T2U2V1WCX2Y17Z17AA17". Please resend!
          1234 > psc844001vr15rc102h1j1m1n1p1q1r1s1tnovnoynonznonaanon
          1234 < Invalid responses for the checklist code: "TN, YN, NAAN, VN, NZN". You sent: PSC844001VR15RC102H1J1M1N1P1Q1R1S1TN0VN0YN0NZN0NAAN0N
          1234 > psc86001vr15rc269h1j1k1m1n5p5q5r5s1t2u2v1w2x2y8z8aa8@registration started late and very slow
          1234 < Invalid message:"PSC86001VR15RC269H1J1K1M1N5P5Q5R5S1T2U2V1W2X2Y8Z8AA8". Please resend!
        """)

    def testVRIncident(self):
        pass

    def testDCOChecklist(self):
        self.assertInteraction("""
          1234 > psc817001dc14rc999a1b1c3d1e1f5
          1234 < DCO Checklist report accepted! You sent: PSC817001DC14RC999A1B1C3D1E1F5
          1234 > PSC648001DC15RC196A2
          1234 < DCO Checklist report accepted! You sent: PSC648001DC15RC196A2
          1234 > PSC740001DC14RC109A1B1C3D1E1F9G3H1J9999K300M2N2P2Q2R1@impressive
          1234 < DCO Checklist report accepted! You sent: PSC740001DC14RC109A1B1C3D1E1F9G3H1J9999K300M2N2P2Q2R1
          1234 > PSC180002DC14RC122A2B1C2D1E1F12358G13H1J0121K0040M1N1P2Q2R2S0001T0013U0005V0007W0006X0010
          1234 < You are not permitted to send this report. Please confirm the report you are to send.
          1234 > PSC817001DC14RC999A1BC3D1E1F5
          1234 < Invalid responses for the checklist code: "BC". You sent: PSC817001DC14RC999A1BC3D1E1F5
          1234 > PSC366001DC14RC122A2B1C12D1E1F12358G65H1J0121K0040M1N1P2Q2R2S1T13U5V7W6X1
          1234 < Invalid response(s) for question(s): "C, G". You sent: PSC366001DC14RC122A2B1C12D1E1F12358G65H1J0121K0040M1N1P2Q2R2S1T13U5V7W6X1
          1234 > PSC366001DC14RC122A2B1C1D1E1F123589G12H1J0121K0040M1N1P2Q2R2S1T13U5V7W6X1
          1234 < Invalid response(s) for question(s): "F". You sent: PSC366001DC14RC122A2B1C1D1E1F123589G12H1J0121K0040M1N1P2Q2R2S1T13U5V7W6X1
          1234 > PSC366001DC14RC99A2B1C1D
          1234 < Invalid message:"PSC366001DC14RC99A2B1C1D". Please resend!
            """)

    def testDCOIncident(self):
        pass
