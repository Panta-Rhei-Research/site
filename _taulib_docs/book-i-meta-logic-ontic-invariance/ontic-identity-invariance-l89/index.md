---
{
  "projection_kind": "taulib_declaration",
  "title": "ontic_identity_invariance",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/ontic-identity-invariance-l89/",
  "summary_short": "`def` declaration in `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.OnticInvariance::ontic_identity_invariance",
  "declaration_slug": "ontic-identity-invariance-l89",
  "kind": "def",
  "name": "ontic_identity_invariance",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "source_line_start": 89,
  "source_line_end": 95,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L89-L95",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L89-L95",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
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
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L89-L95)
- Source range: L89-L95
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The theorem witness: τ satisfies all conditions. -/
```

## Source Excerpt

```lean
def ontic_identity_invariance : OnticIdentityInvariance where
  profile := tau_resonance
  is_tau := rfl
  l_blocked := rfl
  e_blocked := rfl
  p_blocked := rfl
  all_blocked := blocking_targets_surjective
```
