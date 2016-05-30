from myhdl import block

@block
def txEngine(gtxClk, txData2Engine, , txData2GMII, transmitPauseFrame, sampledPauseVal):
    
    """
    *Transmit Engine*
    Accepts Ethernet frame data from the Client Transmitter interface, adds preamble to the 
    start of the frame, add padding bytes and frame check sequence. It ensures that the inter-frame 
    spacing between successive frames is at least the minimum specified. The frame is then converted 
    into a format that is compatible with the GMII and sent to the GMII Block.
    
    gtxClk - Reference Clock for Transmit Operations from Host
    txData2Engine - Transmit Data Channel From Client
    transmitPauseFrame - Control Signal from FLowControl to Indicate Sending Pause Control Frame
    txData2GMII - Transmit Data Channel To GMII
    
    """
    
    return instances()
