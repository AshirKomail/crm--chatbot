from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Table: wp_wc_contact_relation_items
class ContactRelationItems(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    subscriber_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_subscribers.id'))
    provider = db.Column(db.String(200))
    value = db.Column(db.String(200))
    value_int = db.Column(db.Integer)
    value_decimal = db.Column(db.DECIMAL(10, 2))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_control_relations
class ControlRelations(db.Model):
    __tablename__ = 'wp_wc_control_relations'
    id = db.Column(db.BigInteger, primary_key=True)
    subscriber_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_subscribers.id'))
    provider = db.Column(db.String(200))
    value = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_subscribers
class Subscribers(db.Model):
    __tablename__ = 'wp_wc_subscribers'
    id = db.Column(db.BigInteger, primary_key=True)
    email = db.Column(db.String(200))
    first_name = db.Column(db.String(200))
    last_name = db.Column(db.String(200))
    status = db.Column(db.String(50))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)
    contact_relations = db.relationship('ContactRelationItems', backref='subscriber', lazy=True)
    control_relations = db.relationship('ControlRelations', backref='subscriber', lazy=True)

# Table: wp_wc_campaigns
class Campaigns(db.Model):
    __tablename__ = 'wp_wc_campaigns'
    id = db.Column(db.BigInteger, primary_key=True)
    funnel_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_funnels.id'))
    email_subject = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_funnels
class Funnels(db.Model):
    __tablename__ = 'wp_wc_funnels'
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(200))
    description = db.Column(db.TEXT)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)
    campaigns = db.relationship('Campaigns', backref='funnel', lazy=True)

# Table: wp_wc_sequence_tracker
class SequenceTracker(db.Model):
    __tablename__ = 'wp_wc_sequence_tracker'
    id = db.Column(db.BigInteger, primary_key=True)
    subscriber_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_subscribers.id'))
    campaign_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_campaigns.id'))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_funnel_subscribers
class FunnelSubscribers(db.Model):
    __tablename__ = 'wp_wc_funnel_subscribers'
    id = db.Column(db.BigInteger, primary_key=True)
    funnel_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_funnels.id'))
    subscriber_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_subscribers.id'))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_subscriber_notes
class SubscriberNotes(db.Model):
    __tablename__ = 'wp_wc_subscriber_notes'
    id = db.Column(db.BigInteger, primary_key=True)
    subscriber_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_subscribers.id'))
    note = db.Column(db.TEXT)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_funnel_sequences
class FunnelSequences(db.Model):
    __tablename__ = 'wp_wc_funnel_sequences'
    id = db.Column(db.BigInteger, primary_key=True)
    funnel_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_funnels.id'))
    sequence_name = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_campaign_emails
class CampaignEmails(db.Model):
    __tablename__ = 'wp_wc_campaign_emails'
    id = db.Column(db.BigInteger, primary_key=True)
    campaign_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_campaigns.id'))
    email_body = db.Column(db.TEXT)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_campaign_utm_metrics
class CampaignUTMMetrics(db.Model):
    __tablename__ = 'wp_wc_campaign_utm_metrics'
    id = db.Column(db.BigInteger, primary_key=True)
    campaign_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_campaigns.id'))
    utm_source = db.Column(db.String(200))
    utm_medium = db.Column(db.String(200))
    utm_campaign = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_smart_links
class SmartLinks(db.Model):
    __tablename__ = 'wp_wc_smart_links'
    id = db.Column(db.BigInteger, primary_key=True)
    subscriber_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_subscribers.id'))
    link = db.Column(db.String(255))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_tags
class Tags(db.Model):
    __tablename__ = 'wp_wc_tags'
    id = db.Column(db.BigInteger, primary_key=True)
    tag_name = db.Column(db.String(200))
    description = db.Column(db.TEXT)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_lists
class Lists(db.Model):
    __tablename__ = 'wp_wc_lists'
    id = db.Column(db.BigInteger, primary_key=True)
    list_name = db.Column(db.String(200))
    description = db.Column(db.TEXT)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_funnel_notices
class FunnelNotices(db.Model):
    __tablename__ = 'wp_wc_funnel_notices'
    id = db.Column(db.BigInteger, primary_key=True)
    funnel_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_funnels.id'))
    notice_message = db.Column(db.TEXT)
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_contact_relation_match
class ContactRelationMatch(db.Model):
    __tablename__ = 'wp_wc_contact_relation_match'
    id = db.Column(db.BigInteger, primary_key=True)
    subscriber_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_subscribers.id'))
    value = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_funnel_trackers
class FunnelTrackers(db.Model):
    __tablename__ = 'wp_wc_funnel_trackers'
    id = db.Column(db.BigInteger, primary_key=True)
    funnel_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_funnels.id'))
    subscriber_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_subscribers.id'))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)

# Table: wp_wc_utm_stores
class UTMStores(db.Model):
    __tablename__ = 'wp_wc_utm_stores'
    id = db.Column(db.BigInteger, primary_key=True)
    campaign_id = db.Column(db.BigInteger, db.ForeignKey('wp_wc_campaigns.id'))
    utm_store_value = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP)
    updated_at = db.Column(db.TIMESTAMP)
