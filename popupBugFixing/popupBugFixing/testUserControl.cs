using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Data;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace popupBugFixing
{
    public partial class testUserControl : UserControl
    {
        public testUserControl()
        {
            InitializeComponent();
        }

        public string getText()
        {
            return textItem.Text;
        }
    }
}
