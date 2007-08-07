import unittest
import wx

import wxtest
import testControl

"""
This file contains classes and methods for unit testing the API of wx.CheckBox

TODO: update/cleanup docs for this class.  They're quite fleshed out, but could
    use a once-over

Methods yet to test:
__init__, Create
"""

class CheckBoxTest(testControl.ControlTest):
    def setUp(self):
        self.app = wx.PySimpleApp()
        self.frame = wx.Frame(parent=None, id=wx.ID_ANY)
        self.LABEL = "This is the Label Text!"
        self.testControl = wx.CheckBox(parent=self.frame, label=self.LABEL)
    
    def test2StateValueFailure(self):
        """Set3StateValue"""
        if wxtest.ASSERTIONS_ON:
            self.assertRaises(wx.PyAssertionError, self.testControl.Set3StateValue,
                                wx.CHK_UNDETERMINED)
        else:
            self.testControl.Set3StateValue(wx.CHK_UNDETERMINED)
    
    def test3StateValue(self):
        """Set3StateValue, Get3StateValue"""
        self.testControl = wx.CheckBox(self.frame, style=wx.CHK_3STATE)
        self.testControl.Set3StateValue(wx.CHK_CHECKED)
        self.assertEquals(wx.CHK_CHECKED, self.testControl.Get3StateValue())
        self.testControl.Set3StateValue(wx.CHK_UNCHECKED)
        self.assertEquals(wx.CHK_UNCHECKED, self.testControl.Get3StateValue())
        self.testControl.Set3StateValue(wx.CHK_UNDETERMINED)
        self.assertEquals(wx.CHK_UNDETERMINED, self.testControl.Get3StateValue())
    
    def testIs3State(self):
        """Is3State"""
        self.assert_(not self.testControl.Is3State())
        self.assert_(not self.testControl.Is3rdStateAllowedForUser())
        self.testControl = wx.CheckBox(self.frame, style=wx.CHK_3STATE)
        self.assert_(self.testControl.Is3State())
        self.assert_(not self.testControl.Is3rdStateAllowedForUser())
    
    # creating a wx.CheckBox with wx.CHK_ALLOW_3RD_STATE_FOR_USER fails on Windows
    # the docs are fleshed out, but do not mention this.
    # assume wx.CHK_3STATE is necessary when wx-assertions is on
    def testIs3rdStateAllowedForUser(self):
        """Is3rdStateAllowedForUser"""
        self.testControl = wx.CheckBox(self.frame, style=wx.CHK_ALLOW_3RD_STATE_FOR_USER |
                                                    wx.CHK_3STATE)
        self.assert_(self.testControl.Is3State())
        self.assert_(self.testControl.Is3rdStateAllowedForUser())
        
    def testLabel(self):
        """GetLabel"""
        # Overrides previous testLabel method
        self.assertEquals(self.LABEL, self.testControl.GetLabel())
    
    def testValueBoolean(self):
        """SetValue, GetValue, IsChecked"""
        self.assert_(not self.testControl.GetValue())
        self.assert_(not self.testControl.IsChecked())
        self.testControl.SetValue(True)
        self.assert_(self.testControl.GetValue())
        self.assert_(self.testControl.IsChecked())
        self.testControl.SetValue(False)
        self.assert_(not self.testControl.GetValue())
        self.assert_(not self.testControl.IsChecked())
    
    def testValueConstants(self):
        """SetValue, GetValue, IsChecked"""
        # TODO: docs can be updated with this functionality
        self.testControl.SetValue(wx.CHK_CHECKED)
        self.assert_(self.testControl.GetValue())
        self.assert_(self.testControl.IsChecked())
        self.testControl.SetValue(wx.CHK_UNCHECKED)
        self.assert_(not self.testControl.GetValue())
        self.assert_(not self.testControl.IsChecked())
        
        
if __name__ == '__main__':
    unittest.main()