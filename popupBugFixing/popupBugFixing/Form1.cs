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
    public delegate void dataTransfer(testUserControl[] data);

    public partial class Form1 : Form
    {
        public static Form1 Self;
        private testUserControl[] controlArr = null;

        promptForm form = null;
        public dataTransfer transferDelegate;

        public Form1()
        {
            Self = this;
            InitializeComponent();
            transferDelegate += new dataTransfer(getValues);
        }

        public void getValues(testUserControl[] arr)
        {
            controlArr = new testUserControl[arr.Length];
            controlArr = arr.ToArray();
        }

        private void goButton_Click(object sender, EventArgs e)
        {
            form = new promptForm(transferDelegate);
            form.Show();
        }

        private void loadButton_Click(object sender, EventArgs e)
        {
            for(int i = 0; i < controlArr.Length; i++)
            {
                outputListBox.Items.Add("array["+i+"] Returned: "+ controlArr[i].getText());
            }
        }
    }
}
