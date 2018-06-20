using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace popupBugFixing
{
    public partial class promptForm : Form
    {

        private testUserControl[] controls;
        dataTransfer transferDel;
        public promptForm(dataTransfer del)
        {
            InitializeComponent();
            transferDel = del;
            int numItems = Convert.ToInt32(Form1.Self.numItemsText.Text);
            controls = new testUserControl[numItems];

            // Create the UserControls
            for (int i = 0; i < numItems; i++)
            {
                controls[i] = new testUserControl();
            }

            // Place them
            for (int i = 0; i < numItems; i++)
            {
                controls[i].Location = new Point(13, (35 + 25 * (i)));
                this.Controls.Add(controls[i]);
            }
        }

        private void doneButton_Click(object sender, EventArgs e)
        {
            transferDel.Invoke(controls);
            //Close();
        }
    }
}
