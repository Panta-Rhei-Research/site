---
{
  "projection_kind": "taulib_declaration",
  "title": "execOp",
  "permalink": "/verify/taulib/docs/book-iii-spectrum-ttm/exec-op/",
  "summary_short": "`def` declaration in `TauLib.BookIII.Spectrum.TTM`.",
  "declaration_id": "TauLib.BookIII.Spectrum.TTM::execOp",
  "declaration_slug": "exec-op",
  "kind": "def",
  "name": "execOp",
  "module_name": "TauLib.BookIII.Spectrum.TTM",
  "module_url": "/verify/taulib/docs/book-iii-spectrum-ttm/",
  "source_line_start": 171,
  "source_line_end": 197,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L171-L197",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIII.Spectrum.TTM",
        "url": "/verify/taulib/docs/book-iii-spectrum-ttm/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L171-L197",
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

- Module: [TauLib.BookIII.Spectrum.TTM](/verify/taulib/docs/book-iii-spectrum-ttm/)
- Source path: [`TauLib/BookIII/Spectrum/TTM.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIII/Spectrum/TTM.lean#L171-L197)
- Source range: L171-L197
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Execute a single TTM operation on a configuration. -/
```

## Source Excerpt

```lean
def execOp (c : TTMConfig) (op : TTMOp) : TTMConfig :=
  match op with
  | .rho i j =>
    -- r_i := rho(r_j) = r_j + 1 (successor on TauIdx)
    let v := readReg c.registers j + 1
    { c with registers := writeReg c.registers i v }
  | .sigma i j =>
    -- r_i := sigma(r_j) = r_j - 1 (predecessor, truncated at 0)
    let v := readReg c.registers j - 1
    { c with registers := writeReg c.registers i v }
  | .mul i j k =>
    -- r_i := r_j * r_k
    let v := readReg c.registers j * readReg c.registers k
    { c with registers := writeReg c.registers i v }
  | .wedge i j k =>
    -- r_i := min(r_j, r_k)
    let v := min (readReg c.registers j) (readReg c.registers k)
    { c with registers := writeReg c.registers i v }
  | .readPort i j =>
    -- r_i := read(p_j)
    let v := readReg c.ports j
    { c with registers := writeReg c.registers i v }
  | .writePort j i =>
    -- write(p_j, r_i)
    let v := readReg c.registers i
    { c with ports := writeReg c.ports j v }
  | .noop => c
```
