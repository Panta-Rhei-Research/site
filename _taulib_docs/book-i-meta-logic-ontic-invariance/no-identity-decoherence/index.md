---
{
  "projection_kind": "taulib_declaration",
  "title": "no_identity_decoherence",
  "permalink": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/no-identity-decoherence/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.MetaLogic.OnticInvariance`.",
  "declaration_id": "TauLib.BookI.MetaLogic.OnticInvariance::no_identity_decoherence",
  "declaration_slug": "no-identity-decoherence",
  "kind": "theorem",
  "name": "no_identity_decoherence",
  "module_name": "TauLib.BookI.MetaLogic.OnticInvariance",
  "module_url": "/verify/taulib/docs/book-i-meta-logic-ontic-invariance/",
  "source_line_start": 122,
  "source_line_end": 123,
  "registry_ids": [
    "I.C03"
  ],
  "related_registry_items": [
    {
      "id": "I.C03",
      "title": "No Identity Decoherence",
      "url": "/registry/object/I.C03/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L122-L123",
  "formal_status": "formalized",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L122-L123",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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
- Source path: [`TauLib/BookI/MetaLogic/OnticInvariance.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/MetaLogic/OnticInvariance.lean#L122-L123)
- Source range: L122-L123
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `I.C03` — No Identity Decoherence

## Immediate Comment / Docstring

```lean
/-- [I.C03] No Identity Decoherence: the diagonal resonance pattern (L+E+P)
    cannot occur at the ontic level in τ. Direct consequence of I.T46. -/
```

## Source Excerpt

```lean
theorem no_identity_decoherence :
    tau_resonance.isFullResonance = false := tau_no_full_resonance
```
