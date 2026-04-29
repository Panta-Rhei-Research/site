---
{
  "projection_kind": "taulib_declaration",
  "title": "LegitimacyConditions",
  "permalink": "/verify/taulib/docs/book-vii-social-ontology/legitimacy-conditions/",
  "summary_short": "`structure` declaration in `TauLib.BookVII.Social.Ontology`.",
  "declaration_id": "TauLib.BookVII.Social.Ontology::LegitimacyConditions",
  "declaration_slug": "legitimacy-conditions",
  "kind": "structure",
  "name": "LegitimacyConditions",
  "module_name": "TauLib.BookVII.Social.Ontology",
  "module_url": "/verify/taulib/docs/book-vii-social-ontology/",
  "source_line_start": 319,
  "source_line_end": 332,
  "registry_ids": [
    "VII.P25"
  ],
  "related_registry_items": [
    {
      "id": "VII.P25",
      "title": "Legitimacy as Recognition Coherence",
      "url": "/registry/object/VII.P25/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L319-L332",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Social.Ontology",
        "url": "/verify/taulib/docs/book-vii-social-ontology/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L319-L332",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookVII.Social.Ontology](/verify/taulib/docs/book-vii-social-ontology/)
- Source path: [`TauLib/BookVII/Social/Ontology.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Social/Ontology.lean#L319-L332)
- Source range: L319-L332
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `VII.P25` — Legitimacy as Recognition Coherence

## Immediate Comment / Docstring

```lean
/-- [VII.P25] Legitimacy as Recognition Coherence (ch104). 5 conditions:
    (1) Claim: authority A claims power P over domain D — presheaf data
    (2) Recognition: affected entities recognize P — structural prerequisite
    (3) Coherence: recognition sections glue coherently — sheaf condition
        (τ-effective via VII.T31 CI-Sheaf Equivalence)
    (4) Justification: P survives CI universalizability test
        (τ-effective via VII.T35 CI as j-Closed Fixed Point)
    (5) Dignity: exercise of P factors through L_dig
        (τ-effective via VII.T30 Dignity Universality)

    SCOPE UPGRADE: conjectural → τ-effective (Sprint R8-C2).
    Conditions 1–2 are presheaf data (structural prerequisites).
    Conditions 3–5 are applications of already τ-effective CI/dignity machinery. -/
```

## Source Excerpt

```lean
structure LegitimacyConditions where
  /-- (1) Authority claim exists. -/
  has_claim : Bool := true
  /-- (2) Recognition by affected entities. -/
  has_recognition : Bool := true
  /-- (3) Coherence: recognition sections glue (sheaf condition). -/
  coherence_gluing : Bool := true
  /-- (4) Justification: survives CI test. -/
  ci_justified : Bool := true
  /-- (5) Dignity: factors through L_dig. -/
  dignity_preserving : Bool := true
  /-- All 5 conditions satisfied. -/
  condition_count : Nat := 5
  deriving Repr
```
