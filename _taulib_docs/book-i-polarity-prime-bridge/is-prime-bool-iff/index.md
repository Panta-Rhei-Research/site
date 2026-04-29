---
{
  "projection_kind": "taulib_declaration",
  "title": "is_prime_bool_iff",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-bridge/is-prime-bool-iff/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimeBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimeBridge::is_prime_bool_iff",
  "declaration_slug": "is-prime-bool-iff",
  "kind": "theorem",
  "name": "is_prime_bool_iff",
  "module_name": "TauLib.BookI.Polarity.PrimeBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-bridge/",
  "source_line_start": 186,
  "source_line_end": 187,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L186-L187",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.PrimeBridge",
        "url": "/verify/taulib/docs/book-i-polarity-prime-bridge/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L186-L187",
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

- Module: [TauLib.BookI.Polarity.PrimeBridge](/verify/taulib/docs/book-i-polarity-prime-bridge/)
- Source path: [`TauLib/BookI/Polarity/PrimeBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L186-L187)
- Source range: L186-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Boolean primality reflects propositional primality. -/
```

## Source Excerpt

```lean
theorem is_prime_bool_iff (p : TauIdx) : is_prime_bool p = true ↔ idx_prime p :=
  ⟨is_prime_of_bool p, bool_of_is_prime p⟩
```
