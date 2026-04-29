---
{
  "projection_kind": "taulib_declaration",
  "title": "interface_width_at",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-interface-width/interface-width-at/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectrum.InterfaceWidth`.",
  "declaration_id": "TauLib.BookIII.Spectrum.InterfaceWidth::interface_width_at",
  "declaration_slug": "interface-width-at",
  "kind": "def",
  "name": "interface_width_at",
  "module_name": "TauLib.BookIII.Spectrum.InterfaceWidth",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-interface-width/",
  "source_line_start": 46,
  "source_line_end": 47,
  "registry_ids": [
    "I.D71"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L46-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.InterfaceWidth",
        "url": "/verify/taulib/docs/book-iii-spectrum-interface-width/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L46-L47",
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

- Module: [TauLib.BookIII.Spectrum.InterfaceWidth](/verify/taulib/docs/book-iii-spectrum-interface-width/)
- Source path: [`TauLib/BookIII/Spectrum/InterfaceWidth.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/InterfaceWidth.lean#L46-L47)
- Source range: L46-L47
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [I.D71] The interface width of a StageFun f at input n:
    the smallest depth d₀ such that the output at stage d₀
    determines all coarser stages via reduction.

    For a tower-coherent function, this always holds at d₀ = k
    for each individual k (by tower coherence). The interface
    width captures the minimum depth at which the function
    "stabilizes" — i.e., computing at deeper stages doesn't
    change the visible output.

    We define it as the depth at which the function's B-sector
    output first equals reduce(n, d₀): the point where the
    function acts as a simple reduction. -/
```

## Source Excerpt

```lean
def interface_width_at (f : StageFun) (n : TauIdx) : TauIdx → Prop :=
  fun d₀ => ∀ k, k ≤ d₀ → f.b_fun n k = reduce (f.b_fun n d₀) k
```
