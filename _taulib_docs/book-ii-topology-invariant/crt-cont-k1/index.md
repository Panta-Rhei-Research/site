---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_cont_k1",
  "permalink": "/corpus/taulib/docs/book-ii-topology-invariant/crt-cont-k1/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Topology.Invariant`.",
  "declaration_id": "TauLib.BookII.Topology.Invariant::crt_cont_k1",
  "declaration_slug": "crt-cont-k1",
  "kind": "theorem",
  "name": "crt_cont_k1",
  "module_name": "TauLib.BookII.Topology.Invariant",
  "module_url": "/corpus/taulib/docs/book-ii-topology-invariant/",
  "source_line_start": 104,
  "source_line_end": 104,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L104-L104",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Topology.Invariant",
        "url": "/corpus/taulib/docs/book-ii-topology-invariant/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L104-L104",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookII.Topology.Invariant](/corpus/taulib/docs/book-ii-topology-invariant/)
- Source path: [`TauLib/BookII/Topology/Invariant.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Topology/Invariant.lean#L104-L104)
- Source range: L104-L104
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- Formal verification
```

## Source Excerpt

```lean
theorem crt_cont_k1 : crt_continuous_check 1 20 = true := by native_decide
```
