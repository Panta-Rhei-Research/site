---
{
  "projection_kind": "taulib_declaration",
  "title": "no_factor_below_of_spec",
  "permalink": "/verify/taulib/docs/book-i-polarity-prime-bridge/no-factor-below-of-spec/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.PrimeBridge`.",
  "declaration_id": "TauLib.BookI.Polarity.PrimeBridge::no_factor_below_of_spec",
  "declaration_slug": "no-factor-below-of-spec",
  "kind": "theorem",
  "name": "no_factor_below_of_spec",
  "module_name": "TauLib.BookI.Polarity.PrimeBridge",
  "module_url": "/verify/taulib/docs/book-i-polarity-prime-bridge/",
  "source_line_start": 105,
  "source_line_end": 108,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L105-L108",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L105-L108",
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
- Source path: [`TauLib/BookI/Polarity/PrimeBridge.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/PrimeBridge.lean#L105-L108)
- Source range: L105-L108
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- If no k in [d, √n] divides n, then no_factor_below n d = true. -/
```

## Source Excerpt

```lean
theorem no_factor_below_of_spec (n d : TauIdx) (hn : n ≥ 2) (hd : d ≥ 2)
    (hspec : ∀ k : TauIdx, k ≥ d → k * k ≤ n → n % k ≠ 0) :
    no_factor_below n d = true :=
  no_factor_below_of_spec_aux n hn (n - d) d rfl hd hspec
```
