'use client';

import { useState, FormEvent } from 'react';

export default function ContactPage() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    subject: '',
    message: '',
  });
  const [status, setStatus] = useState('');

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    const { id, value } = e.target;
    setFormData(prev => ({ ...prev, [id]: value }));
  };

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setStatus('sending');

    try {
      const res = await fetch('/api/contact', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });

      if (res.ok) {
        setStatus('success');
        setFormData({ name: '', email: '', subject: '', message: '' });
      } else {
        setStatus('error');
      }
    } catch (error) {
      setStatus('error');
    }
  };

  return (
    <div className="py-12">
      <div className="text-center">
        <h1 className="text-4xl font-bold text-gray-800">تواصل معنا</h1>
        <p className="mt-2 text-lg text-gray-600">نحن هنا للمساعدة. أرسل لنا استفسارك وسنرد عليك في أقرب وقت.</p>
      </div>

      <div className="mt-12 grid md:grid-cols-2 gap-12">
        {/* Contact Form */}
        <div className="bg-white p-8 rounded-lg shadow-md">
          <form onSubmit={handleSubmit}>
            <div className="mb-4">
              <label htmlFor="name" className="block text-gray-700 font-bold mb-2">الاسم</label>
              <input type="text" id="name" value={formData.name} onChange={handleChange} className="w-full px-3 py-2 border rounded-lg" required />
            </div>
            <div className="mb-4">
              <label htmlFor="email" className="block text-gray-700 font-bold mb-2">البريد الإلكتروني</label>
              <input type="email" id="email" value={formData.email} onChange={handleChange} className="w-full px-3 py-2 border rounded-lg" required />
            </div>
            <div className="mb-4">
              <label htmlFor="subject" className="block text-gray-700 font-bold mb-2">الموضوع</label>
              <input type="text" id="subject" value={formData.subject} onChange={handleChange} className="w-full px-3 py-2 border rounded-lg" required />
            </div>
            <div className="mb-4">
              <label htmlFor="message" className="block text-gray-700 font-bold mb-2">الرسالة</label>
              <textarea id="message" value={formData.message} onChange={handleChange} rows={5} className="w-full px-3 py-2 border rounded-lg" required></textarea>
            </div>
            <button type="submit" disabled={status === 'sending'} className="w-full bg-blue-600 text-white font-bold py-3 rounded-lg hover:bg-blue-700 disabled:bg-gray-400">
              {status === 'sending' ? 'جارِ الإرسال...' : 'إرسال الرسالة'}
            </button>
            {status === 'success' && <p className="text-green-600 mt-4">تم إرسال رسالتك بنجاح!</p>}
            {status === 'error' && <p className="text-red-600 mt-4">حدث خطأ ما. يرجى المحاولة مرة أخرى.</p>}
          </form>
        </div>

        {/* Contact Info */}
        <div className="space-y-8">
          <div className="bg-white p-8 rounded-lg shadow-md">
            <h2 className="text-2xl font-bold text-gray-800">معلومات الاتصال</h2>
            <ul className="mt-4 space-y-2 text-gray-700">
              <li><b>البريد الإلكتروني:</b> info@safedeny.com</li>
              <li><b>الهاتف:</b> +123 456 7890</li>
              <li><b>العنوان:</b> 123 شارع التكنولوجيا، الرياض، المملكة العربية السعودية</li>
            </ul>
            <h3 className="text-xl font-bold mt-6">ساعات العمل</h3>
            <p className="text-gray-700">الأحد - الخميس: 9:00 صباحاً - 6:00 مساءً</p>
          </div>
          <div className="bg-gray-300 h-64 w-full rounded-lg flex items-center justify-center">
            <p className="text-gray-600">مكان مخصص للخريطة التفاعلية</p>
          </div>
        </div>
      </div>
    </div>
  );
}
