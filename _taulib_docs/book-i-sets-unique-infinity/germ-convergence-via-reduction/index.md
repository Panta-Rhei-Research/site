---
{
  "projection_kind": "taulib_declaration",
  "title": "germ_convergence_via_reduction",
  "permalink": "/verify/taulib/docs/book-i-sets-unique-infinity/germ-convergence-via-reduction/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Sets.UniqueInfinity`.",
  "declaration_id": "TauLib.BookI.Sets.UniqueInfinity::germ_convergence_via_reduction",
  "declaration_slug": "germ-convergence-via-reduction",
  "kind": "theorem",
  "name": "germ_convergence_via_reduction",
  "module_name": "TauLib.BookI.Sets.UniqueInfinity",
  "module_url": "/verify/taulib/docs/book-i-sets-unique-infinity/",
  "source_line_start": 208,
  "source_line_end": 221,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L208-L221",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Sets.UniqueInfinity",
        "url": "/verify/taulib/docs/book-i-sets-unique-infinity/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L208-L221",
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

- Module: [TauLib.BookI.Sets.UniqueInfinity](/verify/taulib/docs/book-i-sets-unique-infinity/)
- Source path: [`TauLib/BookI/Sets/UniqueInfinity.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Sets/UniqueInfinity.lean#L208-L221)
- Source range: L208-L221
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The convergence mechanism is via primorial reduction maps:
    convergence at depth d means agreement modulo M_d. -/
```

## Source Excerpt

```lean
theorem germ_convergence_via_reduction (seq : Nat -> TauIdx) (d : Nat) (_hd : d ≥ 1)
    (h : exists N, forall i j, i ≥ N -> j ≥ N ->
      reduce (seq i) d = reduce (seq j) d) :
    GermConvergence seq d := by
  obtain ⟨N, hN⟩ := h
  exact ⟨N, fun i j hi hj k hk => by
    -- reduce(seq i)(k+1) = reduce(seq j)(k+1)
    -- Since k < d, we have k+1 <= d, so M_{k+1} | M_d
    -- Therefore: reduce(seq i)(k+1) = reduce(reduce(seq i)(d))(k+1)
    --          = reduce(reduce(seq j)(d))(k+1) = reduce(seq j)(k+1)
    have hle : k + 1 ≤ d := hk
    rw [← reduction_compat (seq i) hle,
        ← reduction_compat (seq j) hle,
        hN i j hi hj]⟩
```
