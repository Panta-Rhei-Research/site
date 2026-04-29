---
{
  "projection_kind": "taulib_declaration",
  "title": "OnticIdentityInvariance",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/ontic-identity-invariance/",
  "summary_short": "`structure` declaration in `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.OnticInvariance::OnticIdentityInvariance",
  "declaration_slug": "ontic-identity-invariance",
  "kind": "structure",
  "name": "OnticIdentityInvariance",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "source_line_start": 74,
  "source_line_end": 86,
  "registry_ids": [
    "I.T46"
  ],
  "related_registry_items": [
    {
      "id": "I.T46",
      "title": "Ontic Identity Invariance",
      "url": "/registry/object/I.T46/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L74-L86",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.MetaLogic.OnticInvariance",
        "url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L74-L86",
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

- Module: [TauLib.BookI.MetaLogic.OnticInvariance](/verify/taulib/docs/book-i-meta-logic-ontic-invariance/)
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L74-L86)
- Source range: L74-L86
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- `I.T46` — Ontic Identity Invariance

## Immediate Comment / Docstring

```lean
/-- [I.T46] Ontic Identity Invariance: in the coherence kernel, every admissible
    construction preserves ontic identity. Formalized as: τ has a blocker for
    each resonance component, and its resonance profile is clean.

    The proof packages together:
    1. K5 blocks (L) — contraction_present = false
    2. NF-confluence blocks (E) — equality_congruence = false
    3. Star-autonomous blocks (P) — self_products = false -/
```

## Source Excerpt

```lean
structure OnticIdentityInvariance where
  /-- τ's resonance profile -/
  profile : DiagonalResonance
  /-- The profile matches τ -/
  is_tau : profile = tau_resonance
  /-- (L) is blocked -/
  l_blocked : profile.contraction_present = false
  /-- (E) is blocked -/
  e_blocked : profile.equality_congruence = false
  /-- (P) is blocked -/
  p_blocked : profile.self_products = false
  /-- All three blocking mechanisms exist -/
  all_blocked : ∀ c : ResonanceComponent, ∃ m : BlockingMechanism, blocking_targets m = c
```
