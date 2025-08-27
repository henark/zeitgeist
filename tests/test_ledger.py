from agents.vibe_coder.ledger import Ledger
import tempfile, json
def test_append():
    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        led = Ledger(f.name)
        led.append({"coh": 0.8})
        assert json.loads(open(f.name).readlines()[-1])["coh"] == 0.8
