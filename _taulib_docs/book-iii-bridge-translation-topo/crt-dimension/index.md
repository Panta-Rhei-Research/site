---
{
  "projection_kind": "taulib_declaration",
  "title": "crt_dimension",
  "permalink": "/verify/taulib/docs/book-iii-bridge-translation-topo/crt-dimension/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Bridge.TranslationTopo`.",
  "declaration_id": "TauLib.BookIII.Bridge.TranslationTopo::crt_dimension",
  "declaration_slug": "crt-dimension",
  "kind": "def",
  "name": "crt_dimension",
  "module_name": "TauLib.BookIII.Bridge.TranslationTopo",
  "module_url": "/verify/taulib/docs/book-iii-bridge-translation-topo/",
  "source_line_start": 85,
  "source_line_end": 85,
  "registry_ids": [
    "III.D90"
  ],
  "related_registry_items": [
    {
      "id": "III.D90",
      "title": "Dimension Recovery",
      "url": "/registry/object/III.D90/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L85-L85",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Bridge.TranslationTopo",
        "url": "/verify/taulib/docs/book-iii-bridge-translation-topo/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L85-L85",
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

- Module: [TauLib.BookIII.Bridge.TranslationTopo](/verify/taulib/docs/book-iii-bridge-translation-topo/)
- Source path: [`TauLib/BookIII/Bridge/TranslationTopo.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Bridge/TranslationTopo.lean#L85-L85)
- Source range: L85-L85
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `III.D90` — Dimension Recovery

## Immediate Comment / Docstring

```lean
/-- [III.D90] CRT dimension: number of prime factors at stage k.
    dim(Z/M_k Z) = k (by CRT: Z/M_k ≅ Z/p_1 × ... × Z/p_k). -/
```

## Source Excerpt

```lean
def crt_dimension (k : Nat) : Nat := k
```
