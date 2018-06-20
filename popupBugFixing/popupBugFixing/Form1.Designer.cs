namespace popupBugFixing
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.goButton = new System.Windows.Forms.Button();
            this.outputListBox = new System.Windows.Forms.ListBox();
            this.label1 = new System.Windows.Forms.Label();
            this.numItemsText = new System.Windows.Forms.TextBox();
            this.loadButton = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // goButton
            // 
            this.goButton.Location = new System.Drawing.Point(99, 226);
            this.goButton.Name = "goButton";
            this.goButton.Size = new System.Drawing.Size(75, 23);
            this.goButton.TabIndex = 0;
            this.goButton.Text = "Go";
            this.goButton.UseVisualStyleBackColor = true;
            this.goButton.Click += new System.EventHandler(this.goButton_Click);
            // 
            // outputListBox
            // 
            this.outputListBox.FormattingEnabled = true;
            this.outputListBox.Location = new System.Drawing.Point(45, 34);
            this.outputListBox.Name = "outputListBox";
            this.outputListBox.Size = new System.Drawing.Size(189, 121);
            this.outputListBox.TabIndex = 1;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(45, 182);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(90, 13);
            this.label1.TabIndex = 2;
            this.label1.Text = "How many items?";
            // 
            // numItemsText
            // 
            this.numItemsText.Location = new System.Drawing.Point(141, 179);
            this.numItemsText.Name = "numItemsText";
            this.numItemsText.Size = new System.Drawing.Size(100, 20);
            this.numItemsText.TabIndex = 3;
            // 
            // loadButton
            // 
            this.loadButton.Location = new System.Drawing.Point(99, 5);
            this.loadButton.Name = "loadButton";
            this.loadButton.Size = new System.Drawing.Size(75, 23);
            this.loadButton.TabIndex = 4;
            this.loadButton.Text = "Load Values";
            this.loadButton.UseVisualStyleBackColor = true;
            this.loadButton.Click += new System.EventHandler(this.loadButton_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(284, 261);
            this.Controls.Add(this.loadButton);
            this.Controls.Add(this.numItemsText);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.outputListBox);
            this.Controls.Add(this.goButton);
            this.Name = "Form1";
            this.Text = "Form1";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.Button goButton;
        private System.Windows.Forms.ListBox outputListBox;
        private System.Windows.Forms.Label label1;
        public System.Windows.Forms.TextBox numItemsText;
        private System.Windows.Forms.Button loadButton;
    }
}

